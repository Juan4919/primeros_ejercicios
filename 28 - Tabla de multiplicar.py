'''
Crear un programa que escriba la tabla de multiplicar del número introducido por el usuario, así

Introduzca valor: 5

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

Restricciones
El programa debe impedir la entrada de cualquier número que no sea entero y positivo y volverá a pedirlo

Retos
1 - Formatear la tabla para que los valores salgan en columnas y ajustados a la derecha.
2 - Seguir pidiendo valores hasta que el usuario introduzca un 0 (cero) entonces parar
3 - Plantear solución con while y con for
'''

print("")
print(">>>>>     TABLA DE MULTIPLICAR     <<<<<")
print("")

# Multiplos 
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Obtención de datos y operaciones
while True:
    try: 
        valor = int(input("Introduce el número sobre el que deseas conocer la tabla de multiplicar > "))
        try:
            if valor > 0:
                print("vale")
            break
        except ValueError:
            print("Debes indicar un número superior a cero")            
    except ValueError:
        print("Debes indicar un número ")

print(valor)