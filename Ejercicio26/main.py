input_correct = False
while not input_correct:

    weight = float(input("Introduzca su peso(kg): "))
    #para pasarlo metros diviido entre 100
    height = float(input("Introduzca su altura(cm): "))/100
    if weight<0:
        print("porfavor, introduzca un peso mayor 0 ")
    elif height<0:
        print("porfavor, introduzca una altura mayor 0 ")
    else:
        input_correct=True



body_mass_index= round((weight/(height**2)),2)
print(f"EL indice de masa corporal es de {body_mass_index:.2f}")

