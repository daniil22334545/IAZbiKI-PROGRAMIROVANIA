left = int(input("¬ведите левую грань \n"))
right = int(input("¬ведите правую грань \n"))
numbers = input("¬ведите 3 числа через пробел: ").split(" ")
print("\n \n \n")
for n in range(0,len(numbers)):
    if left<int(numbers[n]) and right>int(numbers[n]):
        print(numbers[n])
