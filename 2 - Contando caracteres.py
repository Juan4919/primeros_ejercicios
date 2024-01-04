'''
El programa pedirá una cadena de caracteres y devolverá el número de caracteres.

Restricciones
Asegurate de que devuelve la cadena original
Utiliza la función específica de python para resolverlo

Retos
1 - Si el usuario no introduce nada, el programa le conminará a que escriba algo.
2 - Hazlo sin utilizar la función específica de python
'''

print("")
print(">>>>>     CONTANDO CARACTERES     <<<<<")
print("")

while True:
    caracter = input("Introduce una palabra o un número determinado de caracteres ")
    if caracter:
        print(caracter, "tiene" , len(caracter),"caracteres") 
        break 
    else: 
        print("No has indicado ningún caracter, por favor introduce de nuevo")
