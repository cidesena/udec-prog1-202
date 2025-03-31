import random
lista=[1,2,3]
t1=tuple(lista)
print(type(t1))

#lista.append(567)
#tupla=()
tupla=(12,13,14,15)
print(type(tupla))
print(tupla[0])
print(tupla[-1])
for dato in tupla:
    print(dato)

tupla=tupla+(16,)
print(tupla)

tupla1=()
cantidad=random.randint(5,15)
for i in range(cantidad):
    num=random.randint(1,100)
    tupla1=tupla1+(num,)

print(tupla1)
l1=list(tupla1)
print(type(l1))

