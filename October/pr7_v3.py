import math
def gip(a,b):
    return math.sqrt(a**2 +b**2)
kat1 = int(input("������ ����� ������� ������������ "))
kat2 = int(input("������ ����� ������� ������������ "))
kat3 = int(input("������ ����� ������� ������������ "))
kat4 = int(input("������ ����� ������� ������������ "))
print(max(gip(kat1,kat2),gip(kat3,kat4)))


