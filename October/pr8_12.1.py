n = int(input("Количество строк "))
m = int(input("Количество столбцов "))
print("\n")
a = [[] for _ in range(m)]
print("Вводите элементы ")
for e in range(n):
    for u in range(m):
        a[e].append(int(input()))
for r in range(len(a)):
    for i in range(len(a)):
            if (a[r][i] == r+1 and a[r][i] == i+1):
                print("Число "+str(a[r][i])+" являеться таким")
                
                
    

