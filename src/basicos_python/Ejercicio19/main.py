number = int(input("Introduce un numero "))
for i in range(number,-1,-1):
    if i == 0:
        print(i)
    else:
        print(i, end=", ")