""" Problema 8:
Escribe  una  función  de  Python  para  calcular  el  factorial  de  un  número  (un  entero  no  negativo).  La función acepta el número como argumento. """

def factorial(numero):
    if numero < 0:
        return "El factorial no está definido para números negativos"
    elif numero == 0 or numero == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, numero + 1):
            resultado *= i
        return resultado


numero = int(input("Ingrese un número entero no negativo para calcular su factorial: "))

resultado_factorial = factorial(numero)
print(f"El factorial de {numero} es: {resultado_factorial}")
