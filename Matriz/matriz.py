import random

#definicion de la matriz
col=5
filas=5

#generacion de la matriz
def generar_matriz():
    matriz=[[random.randint(0,10) for i in range(col)] for j in range(filas)]
    return matriz
