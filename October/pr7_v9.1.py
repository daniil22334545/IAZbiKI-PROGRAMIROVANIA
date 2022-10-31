cicl = 0
def suma(i,cicl):
    if int(i) == 0:
        return cicl
    else:
        x = int(i)
        for num in i:
            x = x-int(num)
        cicl+=1
        return suma(str(x),cicl)
print(suma(input(),cicl))
