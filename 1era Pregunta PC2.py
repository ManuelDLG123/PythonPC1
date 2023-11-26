# Problema 1:
#Escribe  un  programa  en Python para encontrar los números que son divisibles 
#por 7 y múltiplos de 5, en el rango de 1500 y 2700 (ambos incluidos).

rango=1500

while rango <= 2700 :
    if rango % 7==0 and rango % 5==0:
        print(rango)
    rango +=1


