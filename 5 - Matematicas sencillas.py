'''
Escribe un programa que pida dos números y que devuelva su suma, resta, producto y división.

Restricciones
Convertir las cadenas de entrada en números
Separar convenientemente la entrada, transformación de cadena en números y salida separados
Crea una única sentencia de salida con los saltos de línea adecuados (sólo un print)

Retos
1 - Controla que las entradas sean números de forma que el programa no avance si no se introduce un número
2 - No permitas introducir números negativos
'''

print("")
print(">>>>>     OPERACIONES ARITMÉTICAS     <<<<<")
print("")

while True:
    numero1 = input("Introduce un número > ")
    try:
        numero1 = int(numero1)
        if numero1 > 0:
            break
        else:
            print("Por favor, introduce un número positivo")
    except: 
        print("Por favor introduce un número válido")
while True: 
    numero2 = input("introduce otro número > ")
    try:
        numero2 = int(numero2)
        if numero2 > 0:
            break
        else:
            print("Por favor, introduce un número positivo")
    except: 
        print("Por favor introduce un número válido")
print()
while True:
    resultado = input("Ahora indicame la operación que quieres realizar\n 1 - Suma\n 2 - Resta\n 3 - Producto\n 4 - División\n >>> ")
    print()
    if resultado == "1":
        print("El resultado de la suma es", numero1 + numero2)
    elif resultado == "2":
        print("El resultado de la resta es", numero1 - numero2)
    elif resultado == "3":
        print("El resultado del producto es", numero1 * numero2) 
    elif resultado == "4":
        print("El resultado de la división es", numero1 / numero2) 
        break
    else:
        print()
        print("Debes introducir un número según la operación a realizar")
        
