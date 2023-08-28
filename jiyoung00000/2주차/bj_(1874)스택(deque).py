# deque 풀이
from collections import deque
import sys # input()보다 빠르게 입력받기 위함

n = int(sys.stdin.readline()) # 명령의 수

deq = deque()

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0]=='push':
        deq.append(command[1])
    elif command[0]=='pop':
        if len(deq)==0:
            print(-1)
        else:
            print(deq.pop())
    elif command[0] == 'size':
        print(len(deq))
    elif command[0] == 'empty':
        if len(deq)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(deq)==0:
            print(-1)
        else:
            print(deq[-1])