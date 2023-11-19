# Heap
import sys
import heapq as hq

heap = []
n = int(sys.stdin.readline())
for _ in range(n):
    hq.heappush(heap,int(sys.stdin.readline()))

answer = 0
while len(heap) >= 2:
    min1 = hq.heappop(heap)
    min2 = hq.heappop(heap)
    answer+= (min1+min2)
    hq.heappush(heap,min1+min2)
print(answer)