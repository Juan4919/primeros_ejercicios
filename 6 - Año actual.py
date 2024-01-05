'''
Incorpora el año actual al programa. Crea un programa que cuente cuantos años faltan para tu jubilación y que te diga el año en que te jubilarás. Algo así

¿Cuantos años tienes? 48
¿A qué edad te jubilarás? 67
Te quedan 19 años para jubilarte
Estamos en 2018, te jubilarás en 2037.

Restricciones
1 - Convertir las cadenas de entrada en números
2 - Obten el año actual como lo haga python (no vale ponerlo como constante en el programa)

Reto
Maneja la situación si el programa devuelve un número negativo de modo que diga que ya puede jubilarse
'''

print("")
print(">>>>>     CÁLCULO DE LA JUBILACIÓN     <<<<<")
print("")

from datetime import date

edad = int(input("Hola, ¿cuántos años tenes? > "))
print()
jubilar = int(input("¿A que edad te jubilarás? > "))
print()
anyo_actual = date.today().year
print("En ese caso te quedan",jubilar - edad, "años para jubilarte, ya que estamos en", anyo_actual, "y te jubilarás en", edad + anyo_actual)
