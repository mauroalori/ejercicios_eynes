import random 

def generar_lista():
    lista=[{"id":i,"edad":random.randint(0,100)} for i in range (10)]
    return lista