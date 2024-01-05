'''
5 litros de pintura dan para pintar 100 metros cuadrados de techo. Teniendo esto en cuenta haz un programa que diga cuantos botes de 5 litros de pintura hay que 
comprar para pintar un techo de anchura y profundidad informada por el usuario (en metros). Devuelve el número de botes suficiente y por supuesto en números enteros.

Necesitarás 12 litros para pintar 240 metros cuadrados de techo.

Debes comprar 3 botes de pintura.

Restricciones
1 - Utiliza una constante para calcular la conversión botes de pintura/metros de techo
2 - Asegurate de comprar un número entero de botes de pintura suficiente (el siguiente número entero) pero no de más

Retos
1 - Revisar que la entrada sean números positivos. Si no es así no dejar que el usuario continue
2 - Hacer el cálculo para habitación redonda
3 - Hacer el cálculo para habitación en forma de L
'''

print("")
print(">>>>>     CALCULADORA DE PINTURA     <<<<<")
print("")

# Calculo litros de pintura 
ancho = float(input("¿Cuánto es el ancho de la habitación? > "))
print()
profundidad = float(input("¿Cuánto es la profundidad de la habitación? > "))
print()
superficie = round(ancho*profundidad, 2)
litrosNecesarios = round(float((5/100)*superficie), 2)
botesNecesarios = round(litrosNecesarios/5)
print("En base a las medidas indicadas, y dado que tienes que pintar",superficie,"m2, necesitarás",litrosNecesarios,"litros, que equivalen a",botesNecesarios,"botes de pintura")
print()