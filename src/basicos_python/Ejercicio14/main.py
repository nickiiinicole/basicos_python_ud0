age = int(input("Introduce tu edad"))
personal_income = float(input("Introduce tus ingresos"))

if age > 16 and personal_income>=1000:
    print("Debe tributar")
else:
    print("No debe tributar ")