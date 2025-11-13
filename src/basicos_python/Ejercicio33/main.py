def loteria():
    
    list_win_numbers = []
    contador= 0
    number = False
    while len(list_win_numbers)<6:
        win_number= int(input("Introduce el numero ganandor de loteria: "))
        if  1 <= win_number <= 49:#1-49 los nunmeros de loteria
            list_win_numbers.append(win_number)
        else:
            print("Numero invalido, introduzca un numero entre el rango 1 y 49.")
    # sorted -> devuelve otra lista 
    list_win_numbers.sort(reverse=True)
    return list_win_numbers

print(f"El numero de loteria es {loteria()}")