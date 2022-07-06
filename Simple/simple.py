import random 

#cantidad de personas de la lista
cant_personas=10

#funcion para generar la lista
def generar_lista():
    lista=[{"id":i,"edad":random.randint(0,100)} for i in range (cant_personas)]
    return lista

#funcion para ordenar la lista
def ordenar_lista(lista=generar_lista()):
    for i in range(cant_personas-1):
        for j in range(cant_personas-i-1):
            if lista[j]['edad']<lista[j+1]['edad']:
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
    print(f"Edad de la persona mas joven {lista[cant_personas-1]['edad']} \nEdad de la persona mas vieja: {lista[0]['edad']}")
    return lista