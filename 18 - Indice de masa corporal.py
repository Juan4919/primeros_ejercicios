print("")
print(">>>> CALCULADORA DE IMC <<<<")
print("")
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