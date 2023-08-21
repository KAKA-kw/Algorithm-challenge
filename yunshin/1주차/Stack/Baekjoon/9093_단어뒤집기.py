# Stack, Deque
from collections import deque

t = int(input())
MoonJangs = [input() for _ in range(t)]

for moonjang in MoonJangs:
    if len(moonjang) == 1:
        print(moonjang)
        continue
    stack = deque()
    result = []
    for chr in list(moonjang):
        if chr == " ":
            while stack:
                result.append(stack.pop())
            result.append(" ")
        else:
            stack.append(chr)
    while stack:
        result.append(stack.pop())
    print("".join(result))