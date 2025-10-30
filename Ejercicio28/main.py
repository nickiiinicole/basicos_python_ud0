number1 = int(input("Introduce un numero entero: "))
number2 = int(input("Introduce otro un numero entero: "))

def division(divisor, dividendo):
    if divisor== 0 :
        print("No se puede dividir entre 0 . Indeterminación")
        return None #no se si puede usar?¿
    return (dividendo/divisor,  (dividendo%divisor))

result = division(number1, number2)
if result is not None:
    cociente, resto = result  # acordarse de desampaquetar
    print(f"{number1} entre {number2} da un cociente de {cociente} y un resto {resto}")