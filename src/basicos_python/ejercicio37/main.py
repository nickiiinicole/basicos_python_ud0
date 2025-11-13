def ask_user():
    
    name= input("Introduce tu nombre: ")
    age = int(input("Introduce tu edad: "))
    address = input("Introduce tu direccion: ")
    phone_number= (input("Introduce tu telefono: "))

    persona = {
    "nombre": name,
    "edad": age,
    "direccion": address,
    "telefono": phone_number
    }

    return persona

persona = ask_user()
print(f"Tiene {persona['edad']} anos, vive en {persona['direccion']} e o seu numero de telefono é {persona['telefono']}.")

