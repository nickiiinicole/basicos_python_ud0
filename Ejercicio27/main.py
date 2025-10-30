def calculate_bill(quantity, percentage=21):
    #para pasarle el porcentae
    return quantity+(quantity*percentage/100)

print(f"La factura sera de: {calculate_bill(30):.2f}")