n = int(input("���������� ����� "))
m = int(input("���������� �������� "))
print("\n")
a = [[] for _ in range(m)]
for e in range(n):
    for u in range(m):
        a[e].append(int(input()))
        print(a)
a.sort(reverse=True)
for i in a:
    i.sort(reverse=True)
    for j in i:
        print(j, end = ' ')
    print("\n")
