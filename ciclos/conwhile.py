# x=True
# print(type(x))
# #if x
# if x==True:
#     print("Siempre dice la verdad")
# else:
#     print("Es mentiroso")

# while x==True:
#     print("Es verdad infinitamente")


# i=0
# while i<=10:
#     if i%2==0:
#         print(i)
#     i+=1

# cont=0
# num=1
# while num!=0:
#     num=int(input("ingrese numero"))
#     cont+=1
# print(f"ingreso {cont-1} numeros")

#-----------------------------------
# n1=num=int(input("ingrese numero"))
# n2=num=int(input("ingrese numero"))
# mayor=0
# menor=0

# if n1<n2:
#     menor,mayor=n1,n2
# else:
#     menor,mayor=n2,n1
# cont=0
# rta=menor
# while rta<=mayor:    
#     rta+=menor
#     cont+=1
#     #print(f"cont={cont} menor={menor}")
# print(f"Se sumo {cont} veces")

import random
num=1
cont=0
while num%10!=0:
    num=random.randint(1,100)
    print(f"num={num}")
    if num%2==0:
        cont+=1

print(f"la cantidad de pares fue:{cont}")

