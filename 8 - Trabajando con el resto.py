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
