""" Problema 10:
En los Estados Unidos, las fechas suelen tener el siguiente formato: mes-día-año (MM/DD/AAAA). Las fechas en ese formato no se pueden ordenar fácilmente porque el año de la fecha es el último en lugar del primero. Intente ordenar, por ejemplo, 2/2/1800, 3/3/1900 y 1/1/2000 cronológicamente en cualquier programa (por ejemplo, una hoja de cálculo). Las fechas en ese formato también son ambiguas. ¡Una fecha como el 8 de septiembre de 1636, podría interpretarse como el 9 de agosto de 1636!
Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como 8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en la lista abajo:
[
"Enero",
"Febrero",
"Marzo",
"Abril",
"Mayo",
"Junio",
"Julio",
"Agosto",
"Septiembre",
"Octubre",
"Noviembre",
"Diciembre"
]
Luego, genere esa misma fecha en formato AAAA-MM-DD.
Ejemplos:
-          Input: 9/8/1636 | Output: 1636-09-08
-            Input: Septiembre 8, 1636 | Output: 1636-09-08
-          Input: 1/1/1970 | Output: 1970-01-01
Nota:
-          Los métodos de listas y string le resultarán de gran utilidad.
-          Nota que si empleamos print(f"{n:02}") , esta completará con 0 valos a la izquierda de un número """

def obtener_fecha_ordenada(fecha):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]


    partes_fecha = fecha.split()
    

    if len(partes_fecha) == 3:
        mes, dia, anio = partes_fecha
    else:
        mes = partes_fecha[0]
        dia, anio = partes_fecha[1].replace(',', ''), partes_fecha[2]


    indice_mes = meses.index(mes) + 1
    

    dia_formateado = f"{int(dia):02}"
    mes_formateado = f"{indice_mes:02}"


    return f"{anio}-{mes_formateado}-{dia_formateado}"


fecha_input = input("Ingrese la fecha (en formato mes-día-año o mes día, año): ")

fecha_ordenada = obtener_fecha_ordenada(fecha_input)
print("Fecha en formato AAAA-MM-DD:", fecha_ordenada)
