'''
Craer un programa que calcule el indice de masa corporal de una persona según la fórmula

IMC=pesoaltura2

Si el índice de masa corporal está entre 18,5 y 15 el peso se considera normal. Por encima se considera sobrepeso, por debajo delgadez.

Haz un programa que pida ambos datos, devuelva tu índice de masa corporal e indique si estás por encima o por debajo de la normalidad

Restricciones
1 - Impedir que el programa continúe si se introducen datos no numéricos

Retos
1 - Crear una versión que acepte unidades de altura y peso anglosajonas (deberás buscar y cambiar la fórmulas)
2 - Partiendo de la siguiente tabla

Clasificación	IMC
Delgadez Severa	< 16,00
Delgadez Moderada	16,00 - 16,99
Delgadez leve	17,00 - 18,49
Normal	18,50 - 25,00
Preobeso	25,01 - 29,99
Obesidad leve	30,00 - 34,99
Obesidad media	35 - 39,99
Obesidad mórbida	>= 40

Devolver el diagnóstico según el imc.
'''

print("")
print(">>>>>     CALCULADORA DE IMC     <<<<<")
print("")
# Solicitar y validar el peso
while True:
    peso_input = input("INTRODUCE TU PESO \n\n> ")
    if peso_input.replace(".", "", 1).isdigit():
        peso = float(peso_input)
        break
    else:
        print("")
        print("Debes introducir un valor numérico") 
        print("")
        continue
print("")
# Solicitar y validar la unidad de peso
while True:
    unidadpeso = input("¿EN QUÉ UNIDAD HAS INTRODUCIDO TU PESO? \n\n1 - Kilogramos \n2 - Libras \n\n> ")
    if unidadpeso.replace(".", "", 1).isdigit():
        unidadpeso = int(unidadpeso)
        break
    else:
        print("")
        print("Debes pulsar 1 o 2 en función de la unidad utilizada") 
        print("")
        continue
print("")
if unidadpeso == 2:
    peso = peso*0.45359237
elif unidadpeso == 1:
    pass   
# Solicitar y validar la altura
while True:
    altura_input = input("INTRODUCE TU ALTURA \n\n> ")
    if altura_input.replace(".", "", 1).isdigit():
        altura = float(altura_input)
        break
    else:
        print("")
        print("Debes introducir un valor numérico") 
        print("")
        continue
print("")
# Solicitar y validar la unidad de altura
while True:
    unidadaltura = input("¿EN QUÉ UNIDAD HAS INTRODUCIDO TU ALTURA? \n\n1 - Centímetros \n2 - Pulgadas \n\n> ")
    if unidadaltura.replace(".", "", 1).isdigit():
        unidadaltura = int(unidadaltura)
        break
    else:
        print("")
        print("Debes pulsar 1 o 2 en función de la unidad utilizada") 
        print("")
        continue
print("")
if unidadaltura == 1:
    altura = altura / 100.0  # convertir de centímetros a metros
elif unidadaltura == 2:
    pass

#print("Peso:", peso)
#print("Altura:", altura)

imc = round(float(peso/(altura*altura)), 2)
print("")
print("Tu IMC es >",imc)
print("")
if 18.5 <= imc < 25:
    print("!Estás en tu rango de IMC normal!")
elif imc < 18.5:
    print("Deberías comer más, estás por debajo de tu IMC normal")
elif imc >= 25:
    print("Para de comer búfalo, ¡o te corto el pienso!")