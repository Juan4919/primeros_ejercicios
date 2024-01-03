nombre = input("Dime un nombre de un autor > ")
print()
verbo = input("Ahora dime un verbo > ")
print()
adverbio = input("Necesito también un adverbio > ")
print()
adjetivo = input("Dime un adjetivo > ")
print()
while True:
    opcion = input("Por último, ¿que opción deseas? a/b/c > ")
    print()
    if opcion == "a":
        print("Nuestro amigo " + nombre + " siempre ha querido " + verbo + " " + adverbio + " patatas de una forma " + adjetivo) 
    elif opcion == "b":
        print(nombre + " sabe " + verbo + " " + adverbio + " cosas de casa " + adjetivo) 
    elif opcion == "c":
        print("El otro día, " + nombre + " tuvo que " + verbo + " " + adverbio + " muy " + adjetivo) 
        break
    else: 
        print("introduce una de las opciones en minúsculas por favor") 
