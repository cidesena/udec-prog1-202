# x=range(20,0,-2)
# print(x.start)
# print(x.step)
# print(x.stop)
# print(x)

# for i in range(10):
#     print(f"i={i}")

# for j in range(2,20):
#     print(f"j={j}")

# for k in range(30,0,-5):
#     print(f"k={k}")

# for i in range(10):
#     print(f"{i}^2={i**2}")

# cantidad=int(input("ingrese cuantos numeros va a trabajar"))
# num=0
# for i in range(cantidad):
#     num=int(input("ingrese el numero"))
#     print(f"ud ingresó={num}")

# cantidad=int(input("ingrese cuantos numeros va a trabajar"))
# num=0
# sum=0
# mayor=0
# menor=1000000
# for i in range(cantidad):
#     num=int(input("ingrese el numero"))    
#     sum+=num#sum=sum*num
#     if mayor<num:
#         mayor=num
#     if menor>num:
#         menor=num

# print(f"la suma es={sum}")
# print(f"el promedio es={sum/cantidad}")
# print(f"el mayor es ={mayor}")
# print(f"el menor es={menor}")

# tope=int(input("ingrese cuantos numeros va a trabajar"))
# for k in range(1,tope):
#     if(k%7==0):
#         print(f"{k} es multiplo de 7")
#     else:
#         print(k)


#-------------------------------------------
# start=int(input("Ingrese donde inicia"))
# tope=int(input("Ingrese donde termina"))
# if start<tope:
#     for i in range(start,tope):
#         if i%3==0:
#             print(f"{i} es multiplo de 3")
#         else:
#             print(i)
# else:
#     for i in range(start,tope,-1):
#         if i%3==0:
#             print(f"{i} es multiplo de 3")
#         else:
#             print(i)

#-------------------------------------------
# num=int(input("ingrese numero"))
# for i in range(num):
#     print(i,end="-")
# print()
# for i in range(num,0,-1):
#     print(i,end="-")

#-------------------------------------
import random
cantidad=random.randint(5,20)
num=0
sum=0
mayor=0
menor=1000000
for i in range(cantidad):
    num=random.randint(1,100)
    print(num,end=",")
    sum+=num#sum=sum*num
    if mayor<num:
        mayor=num
    if menor>num:
        menor=num

print(f"la suma es={sum}")
print(f"el promedio es={sum/cantidad}")
print(f"el mayor es ={mayor}")
print(f"el menor es={menor}")
