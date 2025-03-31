#lista por comprensión
import random


lista=[100 for i in range(10)]
print(lista)

lista=[i for i in range(10)]
print(lista)

lista=[i*i for i in range(1,11)]
print(lista)

num=random.randint(5,15)
lista=[i for i in range(1,num)]
print(lista)

num=random.randint(5,15)
lista=[random.randint(1,100) for i in range(1,num)]
print(lista)

pares=[x for x in lista if x%2==0]
impares=[x for x in lista if x%2!=0]
print(pares)
print(impares)
# impares=[]
# for x in lista:
#     if x%2==0:
#         print(f"{x} es par")
#         pares.append(x)
#     else:
#         print(f"{x} es impar")
#         pares.append(x)
