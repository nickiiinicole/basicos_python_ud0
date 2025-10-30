
password = 'reinado'
flag = True

while flag:
    password_input= input("Introduce una password ")
    if(password==password_input):
        print("La password es correcta") 
        flag= False
    else:
        print("Incorrecto. Introduzca de nuevo la password")