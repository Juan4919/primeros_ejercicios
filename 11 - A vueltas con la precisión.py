'''
Crear un programa que pase de dolares a euros. El programa pedirá la tasa de cambio de dolares a euros (cuantos euros se necesitan para tener un dolar). El programa debe devolver lo siguiente

X dolares a una tasa de cambio de Y
Total €

Restricciones
1 - Asegúrate de que la entrada se redondea al centavo
2 - Utiliza una única sentencia de salida

Retos
Crea un diccionario de tasas de conversión y pregunta por paises, no por monedas.
'''

print("")
print(">>>>>     CONVERSION DE DIVISAS     <<<<<")
print("")

dict
{"eur":0.9159, "gbp":0.8015, "jpy":148.8315, "inr":83.3387}

strdolares = input("introduce los dolares a convertir > ")
strtasa = input("¿Que tasa de conversión debemos utilizar? > ")
dolares = round(float(strdolares), 2)
tasa = float(strtasa)
total = round(tasa*dolares, 2)


print(dolares, "dolares a una tasa de cambio de",tasa,"lo que haría un total de",total,"€")

