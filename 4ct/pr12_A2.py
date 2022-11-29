def delen(a,b):
    if a>b:
        a = a-b
        return delen(a,b)
    elif a == b:
        return 0
    else:
        return a

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(delen(a,b))
