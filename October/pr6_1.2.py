n = int(input("n= "))
if n>0:
    lst=[-3+6*rand.random() for i in range(n)]
print(lst)
sr=sum(lst)/len(lst)
    for x,k in enumerate(lst):
        if x==0:
            lst[k]=sr
print(lst)