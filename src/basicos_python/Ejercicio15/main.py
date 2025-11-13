name = input("Introduce tu nombre ").upper()
sexo = input("Introduce tu sexo(M|H)").upper()
if (sexo =='M' and name < 'M') or (sexo == 'H' and name > 'N'):
    print(f" {name} Pertenece al grupo A")
else:
    print(f" {name} Pertenece al grupo B")
