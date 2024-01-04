'''
Crear un programa que calcule la media de un conjunto de valores introducido por el usuario. 
Si el usuario entra 0 (cero) se considerará el final de la entrada de valores y se procederá a calcular la media.

Restricciones

1 - El cero no se debe incluir en el cálculo de la media
2 - Si el primer valor introducido es un cero el programa mostrará un mensaje de error
3 - Mantener separadas la entrada, salida y proceso dentro del programa.
4 - Si el valor introducido no es numérico volver a pedirlo
'''

print("")
print(">>>>>     CALCULADORA DE NOTAS     <<<<<")
print("")

# Almacenamiento de datos 
numeros = []

# Introducción de cantidad de valores
valor = int(input("Cuantos valores deseas introducir > "))
print("")

# Introducción de valor de cada de valor
for i in range (valor):
    while True:
        try:
            numero= float(input("Introduce el valor a calcular > "))
            print("")
            if numero < 1:
                print("Debes introducir un número superior a cero")
                print("")
            else:
                numeros.append(numero)
                break
        except ValueError:
            print("El dato no es válido, por favor introduce un número positivo y mayor que 0") 
    
        
# Operaciones con cada valor introducido:
suma = 0
for numero in numeros:
    suma += numero
cantidad_numeros = len(numeros)
media = suma/cantidad_numeros

# Impresión de resultados:
print("En base a los valores que has introducido",numeros,", la media de estos es",round(media, 2))