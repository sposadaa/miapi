from flask import Flask, jsonify, request
from model import *
import logging #Uso de bitacoras en python


app = Flask(__name__)

#Configuracion basica bitacora

#crea un archivo api.log y a;ade las nuevas entradas al final del archivo
logging.basicConfig(filename="api.log", filemode="a", level=logging.INFO)

#creamos el Loggger (permite e registro en la bitacora)
LOGGER = logging.getLogger(__name__)

#Bearer Token Implementarion ---------------

TOKEN= "123456789ABCD" #Rotar cada cierto tiempo

def check_tocken():
    auth = request.headers.get("Authorization")

    #Validar que exista el header
    if not auth:
        return False
    
    #validar formato debe de ser Bearer tocken
    parts = auth.split() #separo Bearer y el token

    #el tama;o debe de ser de 2 y debe de comenzar con la palabra Bearer
    if len(parts)!=2 and parts[0]!="Bearer":
        return False
    
    #validamos el token del header con el token registrado en el api
    return parts[1]==TOKEN




#---------------

#ruta all users GET http://ip:port/v1/users
@app.get("/v1/users")
def get_users():
    #convert users to json
    users_json=[{"name":t.name, "age":t.age} for t in get_data()]
    LOGGER.info("OPERATION OK: Metodo GET Users ejecutado correctamente")
    return jsonify(users_json),200


#ruta insert user POST http://ip:port/v1/users
@app.post("/v1/users")
def insert_user():
    #Secure endpoints
    if not check_tocken():
        LOGGER.warning("AUTH NOT SUCCESS: Bearer token incorrecto")
        return jsonify({"message":"No autorizado"}), 401
    #-----------------------------


    #get body request client
    get_body=request.get_json()

    if get_body: #¿existe el cuerpo?
        name=get_body.get("name")
        age=get_body.get("age")

        if name and age: # nombre y edad existen?
            
            #nombre es alfabeto y edad es un número?
            if str(name).isalpha() and str(age).isdigit(): 
                user=User()
                user.age=int(age)
                user.name=str(name)
                insert_in_memory(user)
                LOGGER.info(f"INSERT SUCCESS: {name}, {age}")
                return jsonify({"message":"ok"}), 201 #Created
            else:
                LOGGER.warning(f"VALUE ERROR: {name} o {age} son invalidos")
                return jsonify({"message": "tipos de dato inválido"}), 400

        else:
            LOGGER.warning("BODY INCOMPLETO: Faltan argumentos en el cuerpo de request")
            return jsonify({"message":"falta name o age en body"}), 400

    else: # si no existe
        return jsonify({"message":"falta body"}),400







#inicia api
if __name__=="__main__":
    app.run(debug=True, port=8080)
 