import random

lista=[]
print(type(lista))

vector=["udec",100,4.5,[1,2,3],"fin"]
#vector.append(222)
print(type(vector))
print(vector[2])
print(vector[-2])
print(f"tamaño lista={len(vector)}")


#------------------------------------
import random
vec=[]
size=random.randint(5,15)
for i in range(0,size):
    num=random.randint(1,100)
    vec.append(num)

print(vec)
print(f"tamaño lista={len(vec)}")
print(f"primer elemento={vec[0]}")
print(f"Ultimo elemento={vec[-1]}")
tam=len(vec)
if tam%2!=0:
    print(f"Del medio={vec[tam//2]}")
else:    
    #media=vec[tam//2]+vec[(tam//2)-1]
    print(f"Los medio={vec[tam//2]}")
    print(f"Los medio={vec[(tam//2)-1]}")
print(vec)
print("posiciones pares")
for i in range(0,tam,2):
    print(vec[i],end=",")

print()
print("posiciones impares")
for j in range(1,tam,2):
    print(vec[j],end=",")