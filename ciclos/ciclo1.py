# x=range(20,0,-2)
# print(x.start)
# print(x.step)
# print(x.stop)
# print(x)

# for i in range(10):
#     print(f"i={i}")

# for j in range(2,20):
#     print(f"j={j}")

# for k in range(5,30,5):
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

tope=int(input("ingrese cuantos numeros va a trabajar"))
for k in range(1,tope):
    if(k%7==0):
        print(f"{k} es multiplo de 7")
    else:
        print(k)
