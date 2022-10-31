n = int(input("Количество строк "))
m = int(input("Количество столбцов "))
print("\n")
a = [[] for _ in range(m)]
print("Вводите элементы ")
for e in range(n):
    for u in range(m):
        a[e].append(int(input()))
        print(a)
for r in range(len(a)):
    for i in range(len(a)):
            if (a[r][i]%2)==0:
                a[r][i]=0
            else:
                a[r][i] = 1
for i in a:
    for j in i:
        print(j, end = ' ')
    print("\n")

    



