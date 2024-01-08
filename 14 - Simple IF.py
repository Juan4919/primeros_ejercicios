'''
Construye un programa que aplique una tasa a un precio en función de donde se aplique. Así si la provincia en la que se aplica es 'VA' (Valencia) se debe incrementar el precio en un 5,5%.
En otro caso no se aplicará esta tasa. La salida debe ser distinta en función de la provincia, así:

Si el precio es 10 €
- Provincia = 'VA':
        El subtotal es 10.00€
        La tasa es 0.55€
        El total es 10.55€

- Provincia != 'VA':
        El total es 10.00€

Restricciones
1 - Implementar este programa usando sólo un if sin usar else
2 - Las cifras en € deben estar redondeadas al céntimo
3 - Utiliza una sola sentencia print para dar el resultado

Retos
1 - Permitir al usuario introducir su provincia en mayúsculas, minúsculas o mixto
2 - Permitir al usuario introducir el nombre completo de su provincia en mayúsculas, minúsculas o mixto
'''

print("")
print(">>>>>     TASA AUTONÓMICA     <<<<<")
print("")

precio= float(input("Introduce el precio que deseas ver > "))
provincia= input("¿En qué provincia deseas revisar la tasa a aplicar? > ").lower()

if provincia == "valencia":
    precio_impuesto = (precio * 1.055) 
    
print("El precio final es",f"{precio_impuesto:.2f}","€")