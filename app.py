from flask import Flask, jsonify, request
from model import *

app = Flask(__name__)


#ruta all users GET http://ip:port/v1/users
@app.get("/v1/users")
def get_users():
    #convert users to json
    users_json=[{"name":t.name, "age":t.age} for t in get_data()]
    return jsonify(users_json),200


#ruta insert user POST http://ip:port/v1/users
@app.post("/v1/users")
def insert_user():
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

                return jsonify({"message":"ok"}), 201 #Created
            else:
                return jsonify({"message": "tipos de dato inválido"}), 400

        else:
            return jsonify({"message":"falta name o age en body"}), 400

    else: # si no existe
        return jsonify({"message":"falta body"}),400







#inicia api
if __name__=="__main__":
    app.run(debug=True, port=8080)
 