'''
Crear un programa que calcule el interés simple, teniendo en cuenta que se calcula con la siguiente fórmula:

A=P⋅(1+rt) 

donde A es la cantidad ganada, P la cantidad invertida, r el interes y t los años transcurridos desde el inicio de la inversión

Tras X años de inversión al Y %, su cantidad debe ser T

Restricciones
1 - La tasa de interés debe introducirse como porcentaje y no decimal, es decir 15 y no 0,15
2 - La inversión debe redondearse al céntimo
3 - La salida debe formatearse como divisa (€)

Retos
1 - Valida que las entradas sean numéricas y que el usuario no pueda continuar si no introduce un número
2 - Modifica el programa para que imprima el valor de la inversión cada año de la misma hasta llegar al valor pedido
'''

print("")
print(">>>>>     CÁLCULO DE INTERÉS SIMPLE     <<<<<")
print("")

strinversion = input("Introduce la cantidad invertida > ")
inversion = round(float(strinversion), 2)
porcentaje = float(input("Introduce el porcentaje de inversión > "))        
años = int(input("¿Cuantos años de inversión han pasado? > " ))
ganancias = inversion*(1 + (porcentaje / 100))**años

print("Las ganancias han sido", round(ganancias, 2),"€")