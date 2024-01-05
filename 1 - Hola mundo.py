'''
Hacer un programa que pida el nombre y te salude por tu nombre

Restricciones
Mantener entrada, salida y concatenación separados

Retos
1 - Escribir el programa sin usar variables
2 - Escribir un programa que devuelva diferentes tipos de saludos a diferentes tipos de persona.
'''

print("")
print(">>>>>     HOLA MUNDO     <<<<<")
print("")

# Entrada de datos
saludo = input("Hola, ¿cómo te llamas? ")

# Salida y concatenación
print("Hola", saludo)
print()

# RETO (escribir sin variables)
print("Hola", input("¿Como te llamas? "))
print()


# RETO (devolver diferentes saludos)
saludo = input("Hola, ¿como te llamas? ")
if saludo == "Juan":
    print("Hola Juan!")
elif saludo == "Antonio":
    print("Hola Antonio, ¿qué tal?")
elif saludo == "Peter":
    print("Que pasa Peter, cuanto tiempo")
elif saludo == "Paula":
    print("Hola Paula, ¡que bueno  verte!")
else: 
    print("Hola, no te conozco")