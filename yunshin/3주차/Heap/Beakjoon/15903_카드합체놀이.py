# Heap
import sys
import heapq as hq

n, m = map(int,sys.stdin.readline().split(" "))
heap = list(map(int,sys.stdin.readline().split(" ")))
hq.heapify(heap)
for _ in range(m):
    first = hq.heappop(heap)
    second = hq.heappop(heap)
    hq.heappush(heap,first+second)
    hq.heappush(heap,first+second)
print(sum(heap))