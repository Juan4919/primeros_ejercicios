'''
Construir un programa que pida una cita y un autor y devuelva una única cadena con la cita entre comillas y el autor.

Restricciones
No usar format ni % ni fstring. Hacerlo concatenando cadenas y escapando caracteres
'''

print("")
print(">>>>>     CITA AUTOR     <<<<<")
print("")

autor = input("Dime un autor o escritor famoso > ")
print()
cita = input("Ahora dime una cita famosa de el > ")
print()
print(autor + (" dijo en su momento ") + '"' + cita + '"')