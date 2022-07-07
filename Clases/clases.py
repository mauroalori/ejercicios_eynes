import math

class circulo:
    def __init__(self,rad):
        if rad>0:
            self.radio=rad
        else:
            print("No es posible tener un radio menor o igual a 0")
    
    #funcion para calcular el área
    def calcular_area(self):
        area=math.pi*pow(self.radio,2)
        return round(area,2)
    
    #funcion para calcular el perímetro
    def calcular_perimetro(self):
        perimetro=2*math.pi*self.radio
        return round(perimetro,2)


radio=float(input("Ingrese el radio del circulo(en cm): "))

flag=True
while(flag):
    if(radio>0):
        Circulo = circulo(radio)
        flag=False
    else:
        print("El radio debe ser mayor a 0, por favor ingreselo nuevamente")
        radio=float(input("Ingrese el radio del circulo(en cm): "))

print(f"Perimetro: {Circulo.calcular_perimetro()}cm")

print(f"Area: {Circulo.calcular_area()}cm²")