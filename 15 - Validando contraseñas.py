import getpass
users=("usuario", "user", "prueba")
password=("pass")

while True:
    usuario = input("Introduce el usuario de acceso > ")
    if usuario not in users:
        print("Usuario incorrecto")
    else:
        break
while True: 
    contraseña = getpass.getpass("Introduce la contraseña > ")
    if contraseña != password:
        print("Contraseña incorrecta")
    else:
        break
if usuario == users and contraseña == password:
    print("")
    print("")
    print("¡Correcto!, ha entrado en el sistema")
    print("")
    print("")