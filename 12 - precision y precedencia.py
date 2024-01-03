strinversion = input("Introduce la cantidad invertida > ")
inversion = round(float(strinversion), 2)
porcentaje = float(input("Introduce el porcentaje de inversión > "))        
años = int(input("¿Cuantos años de inversión han pasado? > " ))
ganancias = inversion*(1 + (porcentaje / 100))**años

print("Las ganancias han sido", round(ganancias, 2),"€")