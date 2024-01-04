'''
Crear un programa que convierta temperatura de Fahrenheita a Celsius y viceversa. El programa pedirá que tipo de conversión queremos y la mostrará.

Las fórmulas de conversión son:

C=(F−32)⋅59 

F=(C⋅95)+32 

Restricciones
1 - Se puede elegir el tipo de conversión en mayúsculas o minúsculas
2 - Reducir el número de sentencias al mínimo y no repetir prints

Retos
1 - Asegurar que las entradas son numéricas
2 - Modificar el programa para que acepte grados Kelvin
'''

print("")
print(">>>>>     CONVERSOR DE TEMPERATURA     <<<<<")
print("")

conversorgrados= input("A que valor deseas convertir; ¿celsius o fahrenheit? > ")
conversor= conversorgrados.lower
if conversor == "celsius":
    grados_fahrenheit= float(input("Introduce el valor a convertir > "))
    grados_celsius= float((grados_fahrenheit-32)*5/9)
    print("El valor introducido son",grados_celsius,"grados celsius")
elif conversor == "fahrenheit":
    grados_celsius= float(input("Introduce el valor a convertir > "))
    grados_fahrenheit= float((grados_celsius*9/5)+32)
    print("El valor introducido son",grados_fahrenheit,"grados fahrenheit")
else:
    print("Ese valor no se contempla en este programa")
    
    
    
    