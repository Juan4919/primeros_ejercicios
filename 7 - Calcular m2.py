'''
Pide la entrada del ancho y profundo de la habitación en metros. Devuelve la superficie en metros cuadrados y en yardas cuadradas (tomando la referencia de aquí).

Restricciones
1 - Mantener los cálculos separados de la salida
2 - Usa una constante para las conversiones de unidades (aquí)

Retos
1 - Fuerza a que las entradas sean numéricas. Si no son numericas el usuario no podrá continuar.
2 - Crea una versión del programa que permita elegir si la entrada va en metros o en yardas
'''

print("")
print(">>>>>     ÁREA DE UN RECTÁNGULO     <<<<<")
print("")

while True:
    ancho = input("Introduce el ancho de la estancia: ")
    print()
    if ancho.isdigit():
            ancho = int(ancho)
            break
    else:
        print("El dato introducido no es un número")
while True:
    profundo = input("Introduce la profundidad de la estancia: ")
    if profundo.isdigit():
            profundo = int(profundo)
            break
    else:
        print("El dato introducido no es un número")   
print()
valor = input("¿Has introducido los datos en yardas o en metros? ").lower()
if valor == "metros":
    print()  
    superficie = ancho*profundo
    superficieYardas = superficie/0.9144
    superficieYardas2 = round(superficieYardas, 2)
    print("La superficie en metros es", superficie,"m2, mientras que la superficie en yardas es",superficieYardas2,"y2")
    print()
else:
    print()
    superficie = ancho*profundo
    superficieMetros = superficie*0.9144
    superficieMetros2 = round(superficieMetros, 2)
    print("La superficie en yardas es", superficie,"y2, mientras que la superficie en metros es",superficieMetros2,"m2")
    print()