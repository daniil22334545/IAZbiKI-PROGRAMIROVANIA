def v():
    a =int(input())
    if a == 0:
        return 0
    else:
        return(max(a,v()))
print(v())
