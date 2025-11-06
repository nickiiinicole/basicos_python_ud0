def foreign_currency():
    currency=  {'Euro':'€', ' Dollar':'$', ' Yen':'¥'}
    currency_user = input("Introduce tu divisa: ").title()
    if currency_user in currency:
        print(f"Tu divisa {currency_user} es: {currency[currency_user]}")
    else:
        print("Esa divisa no esta disponible.")

foreign_currency()
