import random
vec=[]
size=random.randint(5,15)
for i in range(0,size):
    num=random.randint(1,100)
    vec.append(num)

print(vec)
sumpar=0
sumimpar=0
sumatotal=0
for i in range(len(vec)):
    sumatotal+=vec[i]
    if vec[i]%2==0:
        sumpar+=vec[i]
    else:
        sumimpar+=vec[i]

print(f"suma pares={sumpar}")
print(f"suma impares={sumimpar}")
promedio=sumatotal/len(vec)
print(f"suma total={sumatotal}")
print(f"Promedio ={promedio}")

mayor=0
menor=1000000

for x in vec:
    if x>mayor:
        mayor=x
    if x<menor:
        menor=x

print(f"Mayor ={mayor}")
print(f"Menor ={menor}")