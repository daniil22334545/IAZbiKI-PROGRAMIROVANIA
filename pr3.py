left = int(input("������� ����� ����� \n"))
right = int(input("������� ������ ����� \n"))
numbers = input("������� 3 ����� ����� ������: ").split(" ")
print("\n \n \n")
for n in range(0,len(numbers)):
    if left<int(numbers[n]) and right>int(numbers[n]):
        print(numbers[n])
