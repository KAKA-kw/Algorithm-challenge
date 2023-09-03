# Heap
import sys
import heapq as hq

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    li = list(map(int,sys.stdin.readline().split(" ")))
    for idx in range(len(li)):
        if len(heap)< n:
            hq.heappush(heap,li[idx])
        else:
            if heap[0] < li[idx]:
                hq.heappop(heap)
                hq.heappush(heap,li[idx])  
print(min(heap))