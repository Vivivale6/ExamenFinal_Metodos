# Ejercicio 2
# Complete el siguiente codigo para recorrer la lista `x` e imprima
# los numeros impares y que pare de imprimir al encontrar un numero mayor a 800
import numpy as np

x = np.int_(np.random.random(100)*1000)
pares=[]
for i in range (len(x)): 
    valor= x[i] % 2
    
    if (valor==0):
        pares.append(i)        
        

print(pares)



