def positive_integers():
    entero = False
    while not entero:
        number = int(input("Introduce un numero entero positivo: "))
        if number<=0 :
            print("Por favor introduzca un entero positivo")
        else:
            entero = True
    return number            


def factorial(number):
    result= 1 
    if number==1:
        return 1
    else:
    #FORMA DEL PROFE:
    #RETURN N*(FACTORIAL(N-1))
        for i in range(1, number+1):
            result*= i
    return result    


number = positive_integers()
print(f"El factorial de {number} es: {factorial(number)}")
