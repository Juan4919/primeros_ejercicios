'''
Hacer un programa que traduzca los números del 1 al 12 a los meses del año. Hacerlo con if - elif.

Restricciones
1 - Dejar una única instrucción de salida

Retos
1 - Sustituir la selección con una estructura de datos complejos
2 - Hacer el mismo programa en más de un idioma (a elegir por el usuario)
'''

print("")
print(">>>>>     DE NUMERO A MES     <<<<<")
print("")

meses = {
    1: {"español": "Enero", "italiano": "Gennaio", "inglés": "January", "francés": "Janvier", "alemán": "Januar", "portugués": "Janeiro"},
    2: {"español": "Febrero", "italiano": "Febbraio", "inglés": "February", "francés": "Février", "alemán": "Februar", "portugués": "Fevereiro"},
    3: {"español": "Marzo", "italiano": "Marzo", "inglés": "March", "francés": "Mars", "alemán": "März", "portugués": "Março"},
    4: {"español": "Abril", "italiano": "Aprile", "inglés": "April", "francés": "Avril", "alemán": "April", "portugués": "Abril"},
    5: {"español": "Mayo", "italiano": "Maggio", "inglés": "May", "francés": "Mai", "alemán": "Mai", "portugués": "Maio"},
    6: {"español": "Junio", "italiano": "Giugno", "inglés": "June", "francés": "Juin", "alemán": "Juni", "portugués": "Junho"},
    7: {"español": "Julio", "italiano": "Luglio", "inglés": "July", "francés": "Juillet", "alemán": "Juli", "portugués": "Julho"},
    8: {"español": "Agosto", "italiano": "Agosto", "inglés": "August", "francés": "Août", "alemán": "August", "portugués": "Agosto"},
    9: {"español": "Septiembre", "italiano": "Settembre", "inglés": "September", "francés": "Septembre", "alemán": "September", "portugués": "Setembro"},
    10: {"español": "Octubre", "italiano": "Ottobre", "inglés": "October", "francés": "Octobre", "alemán": "Oktober", "portugués": "Outubro"},
    11: {"español": "Noviembre", "italiano": "Novembre", "inglés": "November", "francés": "Novembre", "alemán": "November", "portugués": "Novembro"},
    12: {"español": "Diciembre", "italiano": "Dicembre", "inglés": "December", "francés": "Décembre", "alemán": "Dezember", "portugués": "Dezembro"}
}



#Declaración de variables    
numero_mes = int(input("Introduce el número de mes que quieres conocer > "))
idioma = input("¿En qué idioma deseas conocer el nombre del mes? > " )
idiomas_disponibles = ["italiano", "inglés", "francés", "alemán", "portugués"]

if idioma.lower() in idiomas_disponibles:
    if numero_mes in meses:
        nombre_mes = meses[numero_mes][idioma.lower()]
        print("Has indicado el mes",numero_mes,"que sería",nombre_mes)
        pass







