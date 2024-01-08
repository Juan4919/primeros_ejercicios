'''
Introduciremos aquí los exponentes. En préstamos o inversiones a largo plazo se suele utilizar más el interes compuesto que el simple (diferencias entre ambos). Se trata ahora 
de escribir un programa que calcule el interés compuesto sobre un capital a lo largo del tiempo.

El programa ha de pedir el capital inicial, el interes anual, el número de años de la inversión y el número de veces que se calcula en interés en el año. La fórmula a aplicar es:

A=P(1+rn)nt 

donde

P es el capital inicial
r el interes anual
t los años que dura la inversión (o préstamo)
n el número de veces que se acumula el interés por año (por ejemplo 12 si es mensual)
A es la cantidad al final de la inversión,
Así, para:

1500 € de capital inicial
4,3% de interes
6 años de duración del préstamo
Se calcula el interés al trimestre (4 periodos por año)
El programa debería devolver

1500.00 € invertidos al 4.3% durante 6 años con 4 periodos de imposición por año se transforman en 1938.84 €

Restricciones
1 - El interés se introduce como % no como tanto por uno (15 en lugar de 0.15)
2 - Asegurar que las cantidades en euros estén ajustadas al céntimo

Retos
1 - Impedir que el usuario siga con el proceso si no introduce valores numéricos correctos
2 - Hacer una versión del programa que actúe al revés. Conociendo el tipo de interés, los años y periodos de imposición y sabiendo que suma total se quiere conseguir el programa debe indicar el capital inicial a invertir
'''

print("")
print(">>>>>     CALCULANDO EL INTERÉS COMPUESTO     <<<<<")
print("")

try:
    capital_inicial=float(input("Introduce el capital inicial > "))
    interes_anual=(float(input("¿A que porcentaje de interés será la inversión? > "))/100)
    anyos=int(input("¿Cuántos años de duración tendrá la inversión? > "))
    acumulacion_interes=int(input("¿Cuantas veces al año se calculará el interés al año? > "))
    cantidad_final = capital_inicial * (1 + interes_anual / acumulacion_interes) ** (acumulacion_interes * anyos)

    print("La cantidad final de la inversión será de ",f"{cantidad_final:.2f}")
    print()
except ValueError:
    print("Error: Por favor, asegúrate de ingresar valores numéricos válidos.")
    
print("Variante: obtención del capital inicial")
print()
capital_final=float(input("Introduce el capital final que deseas obtener > "))
interes_anual=(float(input("¿A que porcentaje de interés será la inversión? > "))/100)
anyos=int(input("¿Cuántos años de duración tendrá la inversión? > "))
acumulacion_interes=int(input("¿Cuantas veces al año se calculará el interés al año? > "))
capital_inicial = capital_final / (1 + interes_anual / acumulacion_interes) ** (acumulacion_interes * anyos)

print("La cantidad necesaria para obtener los",capital_final,"€ indicados, serían",f"{capital_inicial:.2f}","€")