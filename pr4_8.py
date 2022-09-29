n = int(input())
i = int(input())
print("\n")
for a in range(n):
	sum = ""
	for q in range(i):
		sum+=str(q)
	print(" "*(a)+sum)
