'''
Introduce 3 números y muestra el mayor

Restricciones
1 - Impedir continuar si no son números
2 - Impedir continuar si no son todos distintos
3 - Hacerlo a mano, sin utilizar funciones del lenguaje que te permitan encontrar el mayor.

Retos
1 - Intentar hacerlo de manera más eficiente con funciones y estructuras de datos
2 - Modificar el programa para hacerlo con 10 números
3 - Modificar el programa para hacerlo con tantos números como el usuario quiera
'''

print("")
print(">>>>>     MÁXIMO VALOR     <<<<<")
print("")

# Métodos
def validar ():
    if primero != segundo and primero != tercero and segundo != tercero:   
            if primero > segundo and primero > tercero: 
                print("el primero es el valor mas alto")
            elif segundo > primero and segundo > tercero: 
                print("El segundo es el número mas alto")
            elif tercero > primero and tercero > segundo: 
                print("El tercero es el numero mas alto")
                return
    else:   
        print("Debes introducir 3 números distintos")

# Declaración de variables
while True:
    try: 
        primero = float(input("Introduce el primer valor > "))
        segundo = float(input("Introduce el segundo valor > "))
        tercero = float(input("Introduce el tercer valor > ")) 
        validar()
        break
    except ValueError:
        print("Debes introducir un numero!")
        
 
 