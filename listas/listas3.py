
import random

def llenarLista(size):
    vec=[]    
    for i in range(0,size):
        num=random.randint(1,100)
        vec.append(num)
    return vec

def sumaLista(lista):
    suma=0
    for n in lista:
        suma+=n
    return suma



t=random.randint(5,20)
milista=llenarLista(t)
print(type(milista))
print(milista)

print(f"la suma de la lista es={sumaLista(milista)}")

