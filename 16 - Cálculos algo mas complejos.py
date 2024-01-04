'''
Crear un programa que obtenga el porcentaje de alcohol en sangre en función de tu género, peso, bebidas y porcentaje de alcohol de las mismas y tiempo transcurrido desde que te las tomaste. Para ello se aplican los siguientes cálculos

Necesitamos conocer los gramos de alcohol ingeridos
Necesitamos saber como se traducen esos gramos de alcohol ingeridos en gramos de alcohol por litro de sangre (alcoholemia)
Lo hacemos asi:

A=Vcc⋅G⋅0,8100 

donde

Vcc es el volumen en centímetros cúbicos de la bebida
G es la graduación de la bebida
0,8 la densidad del alcohol
A son los gramos de alcohol reales que tiene la bebida ingerida
Una vez tenemos los gramos de alcohol absolutos los transformamos en Unidades de Bebida Estándar que es pasarlo a decagramos, es decir 65 gr de alcohol son 6,5 UBE.

Si tenemos las UBE consumidas ¿cómo lo traducimos a alcohol en sangre?. Primero traducimos las UBE en alcoholemia inmediata

ai=UBE⋅0,3 

O dicho de otra manera cada UBE se transforma en 0,3 gramos/litro en sangre según se toma.

Ahora bien, el hígado elimina el alcohol en sangre a una tasa de 0,15 gramos/litro cada hora. Luego la alcolemia real será

aR=ai−0,15⋅H 

donde H son las horas transcurridas desde que tomé y aR es la alcoholemia actual

Lo que queremos es hacer un programa al que le informemos el número de bebidas, su volumen y grado alcohólico y el tiempo transcurrido desde que se tomaron. Con ello el programa debe indicarnos nuestro grado de alcoholemia y si daremos positivo o no en un control.

Así:

Numero de bebidas: 3
Volumen tomado en cc: 40
Grado alcoholico: 35

Otra bebida(S/N): S

Numero de bebidas: 2
Volumen tomado en cc: 200
Grado alcoholico: 8

Otra bebida(S/N): N

Horas transcurridas: 2

Alcohol en sangre: 1.476 g/l

El máximo permitido es 0.5 g/l. 
Usted no puede conducir
En otro caso se indicaría Usted puede conducir

Restricciones
1 - Impedir la entrada de datos no numéricos
'''

print("")
print(">>>>>     ALCOHOL EN SANGRE     <<<<<")
print("")

consumo = int(input("¿Cuantas cervezas te has bebido? > "))
graduacion = float(input("¿Qué graduación tenía la cerveza > "))
vcc = (330*consumo)

tiempo = float(input("¿Hace cuantas horas has dejado de beber? > "))

gramos_alcohol = float(vcc*(graduacion/100)*0.789)
UBE_alcohol = (gramos_alcohol/10)
alcohol_inmediato= (UBE_alcohol*0.3)
alcoholemia_actual= (alcohol_inmediato-0.15)/tiempo

print("")
print("")
print("Actualmente tienes",round(alcoholemia_actual, 3),"mg de alcohol en sangre")
print("")

