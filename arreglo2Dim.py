import numpy as np
import random as rd

matriz = np.zeros((3,3))

#print(matriz)

for f in range(3):
    for c in range(3):
        matriz[f][c] = rd.randint(0,100)

print(matriz)
print("El promedio de los elementos de la matriz es: ", matriz.mean())
print("la suma de los elementos de la matriz es: ", matriz.sum())
print("El elementos mayor de la matriz es: ", matriz.max())
print("El elementos menor de la matriz es: ", matriz.min())
print("los elementos de la diagonal son: ", matriz.diagonal())

arregloDos = np.diag([1,2,3])
print(arregloDos)



