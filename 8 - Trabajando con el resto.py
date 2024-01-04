'''
Escribir un programa que sabiendo cuantas personas hay en una reunión y cuantas pizzas se han comprado, queriendo que cada persona tenga una porción de cada pizza. La pizza sólo puede dividirse en un número par de porciones

¿Número de personas? 7
¿Número de pizzas? 3

7 personas con 3 pizzas
Cada persona toma 3 piezas
Sobran 3 porciones

Retos
1 - Asegurar que la entrada es numerica, positiva y entera. En otro caso impedir que el usuario continue
2 - Escribir los mensajes de salida con formato singular/plural adecuado
'''

print("")
print(">>>>>     REPARTIENDO PIZZA     <<<<<")
print("")

personas = int(input("¿Cuantas personas quieren comer pizza? "))
print()
pizzas = int(input("¿Cuantas pizzas váis a pedir? "))
print()
while True:
    porcionesPizza = int(input("¿Cuantas porciones tiene cada pizza? "))
    if porcionesPizza % 2 == 0: 
        break
    else: 
        print("Todas las pizzas tiene porciones pares, corrige el dato")
print()
porcionesTotal = pizzas * porcionesPizza
porcionesPorPersona = porcionesTotal // personas 
porcionesSobra = porcionesTotal % porcionesPizza
if porcionesSobra == 1:
    print("Dado que hay", personas, "personas, a cada una le tocarán", int(porcionesTotal/personas), "porciones de pizza, por lo que sobrará", porcionesSobra, "porción")
else:
    print("Dado que hay", personas, "personas, a cada una le tocarán", int(porcionesTotal/personas), "porciones de pizza, por lo que sobrarán", porcionesSobra, "porciones")
