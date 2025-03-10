
def potencia(base,exp):
    p=1
    for i in range(1,exp+1):#1, 2, 3
        p=p*base#(3) (9) (27)
    return p

print(potencia(3,3))
print(potencia(2,6))