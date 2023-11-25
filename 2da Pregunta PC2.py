""" Problema 2:
Escriba un programa en Python para construir el siguiente patrón.
*
**
***
****
*****
****
***
**
* """

num_filas = 5
for i in range(1, num_filas + 1):
    print('*' * i)

for i in range(num_filas - 1, 0, -1):
    print('*' * i)
