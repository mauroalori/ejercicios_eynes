import math

class circulo:
    def __init__(self,rad):
        if rad>0:
            self.radio=rad
        else:
            print("No es posible tener un radio menor o igual a 0")

    #funcion para calcular el área
    def calcular_area():
        area=math.pi*pow(self.radio,2)
        return area
    
    #funcion para calcular el perímetro
    def calcular_perimetro():
        perimetro=2*math.pi*self.radio
        return perimetro

