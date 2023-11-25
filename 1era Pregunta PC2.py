# Problema 1:
#Escribe  un  programa  en Python para encontrar los números que son divisibles 
#por 7 y múltiplos de 5, en el rango de 1500 y 2700 (ambos incluidos).

inicio_rango = 1500
fin_rango = 2700

numeros_encontrados = []

for num in range(inicio_rango, fin_rango + 1):
    if num % 7 == 0 and num % 5 == 0:
        numeros_encontrados.append(num)

print("Números divisibles por 7 y múltiplos de 5 en el rango de", inicio_rango, "a", fin_rango, "son:")
print(numeros_encontrados)
