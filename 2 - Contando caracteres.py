while True:
    caracter = input("Introduce una palabra o un número determinado de caracteres ")
    if caracter:
        print(caracter, "tiene" , len(caracter),"caracteres") 
        break 
    else: 
        print("No has indicado ningún caracter, por favor introduce de nuevo")
