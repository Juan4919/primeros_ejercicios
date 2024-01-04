'''
Se trata de crear un programa que pida usuario y contraseña y que valide si coinciden. En el caso de que lo hagan devolver un mensaje Entró en el sistema y en el contrario No te conozco, no pasas

Lo interesante de este programa no es sólo la estructura de if necesarias, sino también la estructura de datos necesaria para almacenar usuarios y sus contraseñas.

Restricciones
1 - Utilizar if/else
2 - Hacer el programa sensible a mayúsculas - minúsculas

Retos
1 - Impide que la contraseña se vea. Investiga para ello
2 - Utiliza un diccionario en lugar de una tupla de tuplas
'''

print("")
print(">>>>>     VALIDANDO CONTRASEÑAS     <<<<<")
print("")

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