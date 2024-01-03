try:
    capital_inicial=float(input("Introduce el capital inicial > "))
    interes_anual=(float(input("¿A que interés será la inversión? > "))/100)
    anyos=int(input("¿Cuántos años de duración tendrá la inversión? > "))
    acumulacion_interes=int(input("¿Cuantas veces al año se calculará el interés al año? > "))
    cantidad_final = capital_inicial * (1 + interes_anual / acumulacion_interes) ** (acumulacion_interes * anyos)

    print("La cantidad final de la inversión será de ", round(cantidad_final, 2))
except ValueError:
    print("Error: Por favor, asegúrate de ingresar valores numéricos válidos.")