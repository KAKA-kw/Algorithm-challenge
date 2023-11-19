# Queue, Deque
from collections import deque

n,k = map(int,input().split())
queue = deque([i+1 for i in range(n)])
answer = []

while queue:
    start = 0 
    while start != (k-1)%len(queue):
        queue.append(queue.popleft())
        start += 1
    answer.append(str(queue.popleft()))
answer = ", ".join(answer)
print("<"+answer+">")