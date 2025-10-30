
#funcion
def sumatorio(number):
    
    return number*(number+1)/2 
#aparte
entero = False 
while not entero:
    number = int(input("Introduce un numero: "))
    if number<=0:
        print("No es un valor entero, por favor vuelta introducirlo ")
    else:
        entero = True

print(f"La Suma de los valores enteros: {sumatorio(number)}")

