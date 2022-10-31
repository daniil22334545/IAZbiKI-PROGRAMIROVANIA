import random
def math(nums):
    suma = 0
    proi = 1
    for num in nums:
        suma+=int(num)
        proi *= int(num)
    suma/=len(nums)
    return "\n Для "+str(nums)+" сред арифм "+str(suma) +" произведение "+str(proi)

a = [random.randint(1,20),random.randint(1,20),random.randint(1,20)]
b = [random.randint(1,20),random.randint(1,20),random.randint(1,20)]
c = [random.randint(1,20),random.randint(1,20),random.randint(1,20)]
print(math(a),math(b),math(c))