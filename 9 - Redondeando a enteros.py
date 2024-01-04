'''
5 litros de pintura dan para pintar 100 metros cuadrados de techo. Teniendo esto en cuenta haz un programa que diga cuantos botes de 5 litros de pintura hay que comprar para pintar un techo de anchura y profundidad informada por el usuario (en metros). Devuelve el número de botes suficiente y por supuesto en números enteros.

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
print(">>>>>     PINTANDO EL TECHO     <<<<<")
print("")

# Calculo litros de pintura 
print(">>> CALCULADORA DE PINTURA <<<")
print()
ancho = int(input("¿Cuánto es el ancho de la habitación)? (en metros) > "))
profundidad = int(input("¿Cuánto es la profundidad de la habitación? (en metros) > "))
superficie = ancho*profundidad
litrosNecesarios = int((5/100)*superficie)
botesNecesarios = litrosNecesarios/5
print()

print("En base a las medidas indicadas, necesitarás", litrosNecesarios, "litros, que equivalen a", round(botesNecesarios), "botes de pintura")