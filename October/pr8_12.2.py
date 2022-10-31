n = int(input("Количество строк "))
m = int(input("Количество столбцов "))
print("\n")
a = [[] for _ in range(m)]
print("Вводите элементы ")
for e in range(n):
    for u in range(m):
        a[e].append(int(input()))
print("Было "+str(a))
for r in range(len(a)-1):
    for i in range(len(a)):
            a[r][i] = a[r][i] - a[n-1][i]
                
print("Стало "+str(a))

