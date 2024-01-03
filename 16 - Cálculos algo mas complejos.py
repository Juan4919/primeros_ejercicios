consumo = int(input("¿Cuantas cervezas te has bebido? > "))
graduacion = float(input("¿Qué graduación tenía la cerveza > "))
vcc = (330*consumo)

tiempo = float(input("¿Hace cuantas horas has dejado de beber? > "))

gramos_alcohol = float(vcc*(graduacion/100)*0.789)
UBE_alcohol = (gramos_alcohol/10)
alcohol_inmediato= (UBE_alcohol*0.3)
alcoholemia_actual= (alcohol_inmediato-0.15)/tiempo

print("")
print("")
print("Actualmente tienes",round(alcoholemia_actual, 3),"mg de alcohol en sangre")
print("")

