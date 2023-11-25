""" Problema 5:
Genere   una   función   que   tenga   como   parámetros   el   ingreso   de   un   número   entero   y   un   dígito. Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.
Ejemplo:
Número ingresado: 15789000 y Dígito: 0
Cantidad de veces 0 en el número: 4
Nota:  Para  resolver  este  problema,  algunos  tipos  de datos dentro de python contemplan un método count. """


def contar_digitos(numero, digito):
    numero_str = str(numero)  
    cantidad = numero_str.count(str(digito)) 
    return cantidad


numero_ingresado = 15789000
digito = 0

resultado = contar_digitos(numero_ingresado, digito)
print(f"Número ingresado: {numero_ingresado} y Dígito: {digito}")
print(f"Cantidad de veces {digito} en el número: {resultado}")
