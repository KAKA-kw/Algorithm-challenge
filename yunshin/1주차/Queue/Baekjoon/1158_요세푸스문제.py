# Queue
n,k = map(int,input().split())
queue = [i+1 for i in range(n)]
answer = []

while queue:
    start = 0
    while start != (k-1)%len(queue):
        queue.append(queue.pop(0))
        start += 1
    answer.append(str(queue.pop(0)))

answer = ", ".join(answer)
answer ="<"+answer+">"
print(answer)