data_in_memory=[]

class User:
    def __init__(self):
        self.name=""
        self.age=0

#métodos de negocio
def insert_in_memory(user:User):
    if user: #¿Si está el usuario?
        data_in_memory.append(user)
        return True
    return False

def get_data():
    return data_in_memory #me regresa los datos en memoria

def delete_user(name:str):
    for t in data_in_memory:
        if t.name == name:
            data_in_memory.remove(t)
            return True
    return False

