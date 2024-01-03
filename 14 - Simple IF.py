precio= float(input("Introduce el precio que deseas ver > "))
provincia= input("¿En qué provincia deseas revisar la tasa a aplicar? > ")

if provincia == "Valencia" or "valencia":
    precio = (precio + 0.55) 
    
print("El precio",precio,"es el valor final aplicado.")