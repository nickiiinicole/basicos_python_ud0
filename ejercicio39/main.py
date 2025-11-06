def shopping_list_show():
    shopping_list = {}
    total = 0

    print("Si deseas terminar escribe 'Fin'\n")
    input_valid = False

    while not input_valid:
        name_item = input("Introduce el nombre del articulo: ").title()
        if name_item.lower() == "fin":
            input_valid = True
            break

        price_item = float(input("Introduce el precio del articulo: "))
        if price_item < 0:
            print("El precio no puede ser negativo.")
            continue

        if name_item in shopping_list:
            print(f"{name_item} ya está en la lista, se actualizará el precio.")

        shopping_list[name_item] = price_item  

    print("\nLISTA DE LA COMPRA")
    print(f"{'ARTICULO':<15} {'PRECIO':>10}")
    print("-" * 26)

    for name, price in shopping_list.items():
        print(f"{name:<15} {price:>8.2f}")
        total += price

    print("-" * 26)
    print(f"{'TOTAL':<15} {total:>10.2f}")


shopping_list_show()
