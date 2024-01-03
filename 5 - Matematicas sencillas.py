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
resultado = input("Ahora indicame el número de la operación quieres realizar\n 1 - Suma\n 2 - Resta\n 3 - Producto\n 4 - División\n >>> ")
print()
if resultado == "1":
    print("El resultado de la suma es", numero1 + numero2)
elif resultado == "2":
    print("El resultado de la resta es", numero1 - numero2)
elif resultado == "3":
    print("El resultado del producto es", numero1 * numero2) 
elif resultado == "4":
    print("El resultado de la división es", numero1 / numero2) 
print()
print("Gracias por participar, perro")
