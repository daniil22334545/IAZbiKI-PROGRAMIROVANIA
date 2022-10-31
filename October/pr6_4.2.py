import random 
mass = [random.randint(0, 10) for _ in range(10)] 
print(mass) 
res = [] 
for el in mass: 
    if el % 2 != 0: 
        res.append(el) 
if len(res) == 0: 
    print('No numbers') 
 
print(sorted(res, reverse=True))