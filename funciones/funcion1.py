def saludo():
    return "Hola como estas"

def saludov2():
    print("Hola como estas v2")

def saludov3(nombre):
    return f"Hola {nombre} como estas"

print(saludov3("Alberto"))
print(saludov3("Maria"))
print(saludov3("Julia"))

# print(saludo())
# variable=saludo()
# print(saludov2())
#print(f"contenido de variable={variable}")

def sumaNumeros(num):
    suma=0
    for i in range(num+1):
        suma+=i
    return suma 

print(sumaNumeros(5))
print(sumaNumeros(100))
print(sumaNumeros(1000))
    
def cantidadNum(num):
    suma=0    
    i=0
    while suma<num:        
        i+=1
        suma=suma+i
    return i

n=int(input("ingrese numero"))
print(cantidadNum(n))
n=int(input("ingrese numero"))
print(cantidadNum(n))
n=int(input("ingrese numero"))
print(cantidadNum(n))    

def Cualmes(dias):
    if dias<=31:
        return "enero"
    elif dias<=59:
        return "febrero"
    elif dias<=90:
        return "marzo"
    elif dias<=120:
        return "abril"
    elif dias<=151:
        return "mayo"
    elif dias<=181:
        return "junio"
    else:
        return "segundo semestre"

print(Cualmes(100))
print(Cualmes(68))


def potencia(base,exp):
    p=1
    for i in range(1,exp+1):#1, 2, 3
        p=p*base#(3) (9) (27)
    return p

print(potencia(3,3))
print(potencia(2,6))


