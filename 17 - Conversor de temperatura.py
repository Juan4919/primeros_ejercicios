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
    
    
    
    