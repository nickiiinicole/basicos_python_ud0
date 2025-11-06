def show_fruits():
    fruits = {}

    name_fruit = input("Introduce el nombre de la fruta: ").lower()
    kg = float(input("Introduce los kg de la fruta: "))

    if name_fruit in fruits:
        total_price = fruits[name_fruit] * kg
        print(f"El precio de {kg} kg de {name_fruit} es {total_price:.2f} €.")
    else:
        print("Esa fruta no está disponible en el sistema.")

show_fruits()
