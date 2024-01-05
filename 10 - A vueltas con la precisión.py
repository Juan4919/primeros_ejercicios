'''
Haz un programa que aplique un impuesto de 5,5% sobre tres precios introducidos por el usuario. Deben introducirse también el número de ejemplares de producto de cada precio
que se compran. Se debe imprimir el subtotal sin tasas, la tasa y la suma de ambos

Restricciones
Manten separadas las partes de entrada, salida y proceso de tu programa

Retos
1 - Comprobar que la entrada sea numérica e impedir continuar si no es así
2 - Permitir que el programa tenga un número indeterminado de productos y cantidades de entrada
'''

print("")
print(">>>>>     APLICANDO IMPUESTOS     <<<<<")
print("")

# Obtención de datos iniciales
while True:
    try:
        precio_1 = float(input("Introduce el primer precio: "))
        ejemplar_1 = int(input("¿Cuantos ejemplares son?: "))
        precio_2 = float(input("Introduce el segundo precio: "))
        ejemplar_2 = int(input("¿Cuantos ejemplares son?: "))
        precio_3 = float(input("Introduce el tercer precio: "))
        ejemplar_3 = int(input("¿Cuantos ejemplares son?: "))
        if precio_1 > 0 and precio_2 > 0 and precio_3 > 0:
            break
        else:
            print("Debes indicar números positivos y mayores que cero")
    except ValueError: 
        print("Debes indicar un número")

# Obtención de tasas
tasa_1 = (precio_1/100)*5.5
tasa_2 = (precio_2/100)*5.5
tasa_3 = (precio_3/100)*5.5

# Valor total de cada producto
precio_impuesto_1 = float("{:.3f}".format(((precio_1/100)*5.5)+precio_1))
precio_impuesto_2 = float("{:.3f}".format(((precio_2/100)*5.5)+precio_2))
precio_impuesto_3 = float("{:.3f}".format(((precio_3/100)*5.5)+precio_3))

# Impresión final 
print(">>  Resultado  <<")
print()
print(f"- El subtotal del primer producto es {precio_1}\n"
      f"- Al aplicar la tasa del 5.5% se añadirá un importe de {tasa_1}\n"
      f"- El valor final sería de {precio_impuesto_1}\n"
      f"- La suma total con los {ejemplar_1} ejemplares sería {ejemplar_1*precio_impuesto_1}")
print()
print(f"- El subtotal del segundo producto es {precio_1}\n"
      f"- Al aplicar la tasa del 5.5% se añadirá un importe de {tasa_2}\n"
      f"- El valor final sería de {precio_impuesto_2}\n"
      f"- La suma total con los {ejemplar_2} ejemplares sería {ejemplar_2*precio_impuesto_2}")
print()
print(f"- El subtotal del tercer producto es {precio_1}\n"
      f"- Al aplicar la tasa del 5.5% se añadirá un importe de {tasa_3}\n"
      f"- El valor final sería de {precio_impuesto_3}\n"
      f"- La suma total con los {ejemplar_3} ejemplares sería {ejemplar_3*precio_impuesto_3}")