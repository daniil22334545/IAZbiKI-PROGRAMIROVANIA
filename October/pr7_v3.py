import math
def gip(a,b):
    return math.sqrt(a**2 +b**2)
kat1 = int(input("Первый катет первого триугольника "))
kat2 = int(input("Второй катет первого триугольника "))
kat3 = int(input("Первый катет второго триугольника "))
kat4 = int(input("Второй катет второго триугольника "))
print(max(gip(kat1,kat2),gip(kat3,kat4)))


