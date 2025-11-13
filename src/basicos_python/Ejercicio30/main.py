import math

def area_circle(radio):

    return math.pi*radio**2

def volume_cylinder(radio, height):
    return area_circle(radio) * height

radio = float(input("Introduce el radio: "))
height = float(input("Introduce la altura: "))
print(f"El valor del area del circulo es {area_circle(radio):.2f} y el volumen del cilindro: {volume_cylinder(radio,height):.2f}")