n = int(input("���������� ����� "))
m = int(input("���������� �������� "))
print("\n")
a = [[] for _ in range(m)]
print("������� �������� ")
for e in range(n):
    for u in range(m):
        a[e].append(int(input()))
print("���� "+str(a))
for r in range(len(a)-1):
    for i in range(len(a)):
            a[r][i] = a[r][i] - a[n-1][i]
                
print("����� "+str(a))

