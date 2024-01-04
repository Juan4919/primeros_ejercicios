# Diccionario IVA
iva_ue = {
    'Alemania': 19,
    'Austria': 20,
    'Bélgica': 21,
    'Bulgaria': 20,
    'Chipre': 19,
    'Croacia': 25,
    'Dinamarca': 25,
    'Eslovaquia': 20,
    'Eslovenia': 22,
    'España': 21,
    'Estonia': 20,
    'Finlandia': 24,
    'Francia': 20,
    'Grecia': 24,
    'Hungría': 27,
    'Irlanda': 23,
    'Italia': 22,
    'Letonia': 21,
    'Lituania': 21,
    'Luxemburgo': 17,
    'Malta': 18,
    'Países Bajos': 21,
    'Polonia': 23,
    'Portugal': 23,
    'República Checa': 21,
    'Rumanía': 19,
    'Suecia': 25,
}

# Declaración de variables
while True:
    cantidad = input("Introduce la cantidad que deseas consultar > ")
    if cantidad.replace(".", "", 1).isdigit():
        break
    else:
        print("")
        print("Debes indicar un valor entero o decimal") 
        print("")
        continue    

pais = input("¿Sobre que país deseas consultar el IVA? > ")
pais = pais.capitalize()

tasa_iva = iva_ue.get(pais, 'No se encuentra la información de IVA para este país.')

cantidad_final = (int(cantidad)*(tasa_iva/100))+int(cantidad)

print(f"La tasa de IVA en {pais} es del {tasa_iva}%, por lo que el importe introducido",cantidad,"€, tendría un total final de",round(cantidad_final, 2),"€")


