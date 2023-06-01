import numpy as np
import random as rd

arreglo = np.zeros(10) # inicializo el arreglo en ceros
#print(arreglo)

for i in range(len(arreglo)):
    arreglo[i] = rd.randint(1,100)

print(arreglo)

arregloDos = arreglo[:].copy()

print("El número mayor del arreglo es: ",arregloDos.max())
print("El número menor del arreglo es: ",arregloDos.min())
print("la suma de los elementos del arreglo es: ",arregloDos.sum())
print("El promedio de los elementos del arreglo es: ",arregloDos.mean())
print(arregloDos)
