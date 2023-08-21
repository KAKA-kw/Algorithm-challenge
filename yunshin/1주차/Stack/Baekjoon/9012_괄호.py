# Stack
n = int(input())
answer = []
for _ in range(n):
    stack = []
    s = input()
    flag = True

    for c in s:
        if c == ')':
            if not stack:
                flag = False
                break
            elif stack:
                stack.pop()
        elif c == "(":
            stack.append('(')
    if flag and not stack:
        answer.append("Yes")
    elif not flag or stack:
        answer.append("No")

for i in range(n):
    print(answer[i])
