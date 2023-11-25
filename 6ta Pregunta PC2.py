""" Problema 6:
Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
Nota: La secuencia de Fibonacci es la serie de números:
0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
Cada número siguiente se obtiene sumando los dos números anteriores """


def fibonacci(limite):
    fibonacci_series = [0, 1] 

    while True:
        siguiente_numero = fibonacci_series[-1] + fibonacci_series[-2]  # Sumar los dos últimos números
        if siguiente_numero > limite:  # Si el siguiente número supera el límite, terminar el bucle
            break
        fibonacci_series.append(siguiente_numero)

    return fibonacci_series

limite = 50
serie_fibonacci = fibonacci(limite)

print("Serie de Fibonacci hasta", limite, ":")
print(serie_fibonacci)
