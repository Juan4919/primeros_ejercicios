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