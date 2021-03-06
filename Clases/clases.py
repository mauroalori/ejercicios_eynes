import math

#multiplicador del objeto "Circulo"
n= 3

class circulo:
    def __init__(self,rad):
        if rad>0:
            self.radio=round(rad,2)
        else:
            print("No es posible tener un radio menor o igual a 0")
    
    #funcion para calcular el área
    def calcular_area(self):
        """
        Testeando el calculo del area
        ----------------------------------
        >>> test.calcular_area()
        78.54
        """
        area=round(math.pi*pow(self.radio,2),2)
        return area
    
    #funcion para calcular el perímetro
    def calcular_perimetro(self):
        """
        Testeando el calculo del perimetro
        ----------------------------------
        >>> test.calcular_perimetro()
        31.42
        """
        perimetro=round(2*math.pi*self.radio,2)
        return perimetro
    
    def __str__(self):
        return "El radio vale %.2fcm. El perimetro vale %.2fcm. El area vale %.2fcm²." %(self.radio,self.calcular_perimetro(),self.calcular_area())

#se ingresa un valor de radio por linea de comandos y se valida
radio=float(input("Ingrese el radio del circulo(en cm): "))

flag=True
while(flag):
    if(radio>0):
        Circulo = circulo(radio)
        flag=False
    else:
        print("El radio debe ser mayor a 0, por favor ingreselo nuevamente")
        radio=float(input("Ingrese el radio del circulo(en cm): "))

print(Circulo)

#se instancia el circulo con el radio multiplicado por n
if(n>0):
    Circulo_por_n = circulo(Circulo.radio * n)

print(Circulo_por_n)

if __name__ == "__main__":
    import doctest
    doctest.testmod(globs={'test':circulo(5)})