from datetime import date

edad = int(input("Hola, ¿cuántos años tenes? > "))
print()
jubilar = int(input("¿A que edad te jubilarás? > "))
print()
anyo_actual = date.today().year
print("En ese caso te quedan", (anyo_actual + edad) - anyo_actual, "años para jubilarte, ya que estamos en", anyo_actual, "y te jubilarás en", edad + anyo_actual)
