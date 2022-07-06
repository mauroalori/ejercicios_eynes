"""
    Cabe aclarar que ya que no se ha determinado un tipo de secuencia específica se asume que la secuencia a encontrar en la matriz
    se trata de números consecutivos que son una unidad mayor al anterior recorriendo las columnas de arriba hacia abajo o las filas
    de izquierda a derecha.
    Ej:
        1,2,3,4,5. Se considera una secuencia
        5,4,3,2,1. No se considera una secuencia

        1   }
        2   }
        3   } Se considera una secuencia
        4   }
        5   }

        5   }
        4   }
        3   } No se considera una secuencia
        2   }
        1   }
"""

import doctest
import random

#definicion de la matriz
col=5
filas=5

#generacion de la matriz
def generar_matriz():
    matriz=[[random.randint(0,10) for i in range(col)] for j in range(filas)]
    return matriz

#busqueda de posibles secuencias en la matriz
def buscar_secuencia(matriz=generar_matriz()):

    """
    Testeo de la busqueda de secuencias en vertical
    -----------------------------------------------
    >>> buscar_secuencia([[1,2,3,5,4],[2,2,2,2,2],[0,3,1,0,0],[0,4,0,0,0],[0,5,0,0,0]])
    Se encontró una secuencia en vertical
    Posicion incial. fila:2,col:2
    Posicion final. fila:5,col:2
    True
    
    Testeo de la busqueda de secuencias en horizontal
    -------------------------------------------------
    >>> buscar_secuencia([[1,2,3,4,9],[2,2,2,2,2],[0,0,0,0,0],[0,4,0,0,0],[5,5,6,7,8]])
    Se encontró una secuencia en horizontal
    Posicion incial. fila:1,col:1
    Posicion final. fila:1,col:4
    Se encontró una secuencia en horizontal
    Posicion incial. fila:5,col:2
    Posicion final. fila:5,col:5
    True

    Si no se encuentran secuencias la función debe retornar False
    -------------------------------------------------------------
    >>> buscar_secuencia([[1,8,8,8,8],[2,2,2,2,2],[8,7,5,3,1],[0,4,0,0,0],[0,5,0,0,0]])
    False
    """

    secuencia_encontrada=False

    #busqueda horizontal (por fila)
    for i in range(filas):
        cont=1
        for j in range(col-1):
            if cont==1:
                col_inicio=j
            if(matriz[i][j]==(matriz[i][j+1]-1)):
                cont+=1
                if(cont==4):
                    print("Se encontró una secuencia en horizontal")
                    print(f"Posicion incial. fila:{i+1},col:{(col_inicio+1)}")
                    print(f"Posicion final. fila:{i+1},col:{(col_inicio+1)+3}")
                    secuencia_encontrada=True
            else:
                cont=1

    #busqueda vertical (por columna)
    for j in range(col):
        cont=1
        for i in range(filas-1):
            if cont==1:
                fila_inicio=j
            if(matriz[i][j]==(matriz[i+1][j]-1)):
                cont+=1
                if(cont==4):
                    print("Se encontró una secuencia en vertical")
                    print(f"Posicion incial. fila:{(fila_inicio+1)},col:{j+1}")
                    print(f"Posicion final. fila:{(fila_inicio+1)+3},col:{j+1}")
                    secuencia_encontrada=True
            else:
                cont=1

    return secuencia_encontrada

if __name__ == "__main__":
    import doctest
    doctest.testmod()