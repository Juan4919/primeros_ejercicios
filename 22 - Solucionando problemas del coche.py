'''
Introduce 3 números y muestra el mayor

Restricciones
1 - Impedir continuar si no son números
2 - Impedir continuar si no son todos distintos
3 - Hacerlo a mano, sin utilizar funciones del lenguaje que te permitan encontrar el mayor.

Retos
1 - Intentar hacerlo de manera más eficiente con funciones y estructuras de datos
2 - Modificar el programa para hacerlo con 10 números
3 - Modificar el programa para hacerlo con tantos números como el usuario quiera
'''

print("")
print(">>>>>     SOLUCIONANDO PROBLEMAS DEL COCHE     <<<<<")
print("")
arranca = input("¿El vehiculo arranca? \nS/N > ").upper()
print("")
if arranca == "S":
    suena = input("Si el vehiculo arranca, ¿suena un clic-clic? \nS/N > ").upper()
    print("")
    if suena == "S":
        print("Si suena un clic-clic entonces reemplaza la batería")
    elif suena == "N":
        enciende = input("Si no suena un clic-clic, ¿el coche intenta arrancar pero no se enciende? \nS/N > ").upper()
        print("")
        if enciende == "S":
            print("En ese caso revisa las bujías")
        elif enciende == "N":
            cala = input("Entonces, ¿arranca el coche y luego se cala? \nS/N > ").upper()
            print("")
            if cala == "N":
                print("Entonces comprate un coche nuevo")
            elif cala == "S":
                combustible = input("¿Has revisado si tiene el coche inyección de combustible? \nS/N > ").upper()
                print("")
                if combustible == "S":
                    print("Entonces lleva el coche al taller, puede ser algo grave")
                elif combustible == "N":
                    print("Haber empezado por ahi, abre y cierra el starter")
                    print("")
                    print("")
                    print(">>>>>> FIN <<<<<<")
elif arranca == "N":
    bornes = input("Si el coche no arranca, ¿están los bornes de la batería corroídos? \nS/N > ").upper()
    print("")
    if bornes == "S":
        print("En ese caso limpialos y arranca de nuevo")
    elif bornes == "N":
        print("Si no están corroídos tendrás que reemplazar los cables y arrancar de nuevo")
        print("")
        print("")
        print(">>>>>> FIN <<<<<<")
    