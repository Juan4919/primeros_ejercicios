while True:
    ancho = input(">>>>>>>CALCULADORA DE SUPERFICIE<<<<<<<\n \nIntroduce el ancho de la estancia: ")
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
valor = input("¿Has introducido los datos en yardas o en metros? ")
if valor == "metros":
    print()  
    superficie = ancho*profundo
    superficieYardas = superficie/0.9144
    superficieYardas2 = round(superficieYardas, 2)
    print("La superficie en metros es", superficie,"m2, mientras que la superficie en yardas es",superficieYardas2,"y2")
else:
    print()
    superficie = ancho*profundo
    superficieMetros = superficie*0.9144
    superficieMetros2 = round(superficieMetros, 2)
    print("La superficie en yardas es", superficie,"y2, mientras que la superficie en metros es",superficieMetros2,"m2")