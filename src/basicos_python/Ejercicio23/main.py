number = int(input("Introduce un numero: "))

# Los números menores o iguales a 1 no son primo!!!!!
if number <= 1:
    print("El numero no es primo")
else:
    # creamos una flag para que entre
    primo = True
    # creo el bucle apra que vea todos los divisores de 2 
    # hasta
    # el numero-1
    for i in range(2, number):
        if number % i == 0:
            primo = False
            break

    if primo:
        print("El numero es primo")
    else:
        print("El numero no es primo")
