# Stack
n,k = map(int,input().split());
stack = []

for _ in range(n):
	com = input().split()
	if com[0]=='push':
		if len(stack) == k:
			print("Overflow")
		else:
			stack.append(int(com[1]))
	else:
		if stack:
			print(stack.pop())
		else:
			print("Underflow")