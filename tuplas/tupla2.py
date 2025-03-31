import random
lista=[]
tpar=()
timpar=()
cantidad=random.randint(5,15)
for i in range(cantidad):
    num=random.randint(1,100)
    #tupla1=tupla1+(num,)
    lista.append(num)

for dato in lista:
    if dato%2==0:
        tpar=tpar+(dato,)
    else:
        timpar=timpar+(dato,)

print(lista)
print(tpar)
print(timpar)