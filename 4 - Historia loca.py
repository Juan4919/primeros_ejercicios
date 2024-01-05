'''
Crear un programa que pida nombre, verbo, adverbio y adjetivo y con ellos construya una historia. Utilizar una plantilla con los huecos donde colocar el nombre, el verbo, el adverbio
y el adjetivo. Eligiendo bien la plantilla la frase puede resultar absurda y hasta graciosa.

Restricciones
Utilizar un solo print en el programa
Hacer una versión utilizando substitucion

Retos
1 - Introducir más datos para complicar y aumentar la historia
2 - Construye una historia del estilo de los libros de "Construye tu propia aventura" de forma que la historia derive según se elija una u otra opción.
'''

print("")
print(">>>>>     HISTORIA LOCA     <<<<<")
print("")

nombre = input("Dime el nombre de un autor > ")
print()
verbo = input("Ahora dime un verbo > ")
print()
adverbio = input("Necesito también un adverbio > ")
print()
adjetivo = input("Por último dime un adjetivo > ")
print()
while True:
    opcion = input("Por último, ¿que opción deseas? a/b/c > ").lower()
    print()
    if opcion == "a":
        print("Nuestro amigo " + nombre + " siempre ha querido " + verbo + " " + adverbio + " patatas de una forma " + adjetivo) 
        print()
    elif opcion == "b":
        print(nombre + " sabe " + verbo + " " + adverbio + " cosas de casa " + adjetivo) 
        print()
    elif opcion == "c":
        print("El otro día, " + nombre + " tuvo que " + verbo + " " + adverbio + " muy " + adjetivo) 
        print()
        break
    else: 
        print()
        print("Introduce una de las opciones en minúsculas por favor") 
        print()
