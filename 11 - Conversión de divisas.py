dict
{"eur":0.9159, "gbp":0.8015, "jpy":148.8315, "inr":83.3387}

strdolares = input("introduce los dolares a convertir > ")
strtasa = input("¿Que tasa de conversión debemos utilizar? > ")
dolares = round(float(strdolares), 2)
tasa = float(strtasa)
total = round(tasa*dolares, 2)


print(dolares, "dolares a una tasa de cambio de",tasa,"lo que haría un total de",total,"€")

