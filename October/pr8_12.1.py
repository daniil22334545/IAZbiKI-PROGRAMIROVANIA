n = int(input("���������� ����� "))
m = int(input("���������� �������� "))
print("\n")
a = [[] for _ in range(m)]
print("������� �������� ")
for e in range(n):
    for u in range(m):
        a[e].append(int(input()))
for r in range(len(a)):
    for i in range(len(a)):
            if (a[r][i] == r+1 and a[r][i] == i+1):
                print("����� "+str(a[r][i])+" ��������� �����")
                
                
    

