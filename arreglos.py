import numpy as np

arreglo = np.array([3,4,12,4,7])

print(arreglo)

print(arreglo.ndim)
largo = len(arreglo)
print(largo)

print(arreglo.shape)
print(arreglo[2:4])
print(arreglo[1:4:2])
print(arreglo[::2])
print(arreglo[2::1])
print(arreglo[-2])

arreglo2 = [i for i in range(0,5)]
print(arreglo2)

for i in range(len(arreglo)):
    print("arreglo[",i,"]=",arreglo[i])

arreglo3 = np.zeros(10)
arreglo4 = np.ones(10)
print(arreglo3)
print(arreglo4)
    
    







