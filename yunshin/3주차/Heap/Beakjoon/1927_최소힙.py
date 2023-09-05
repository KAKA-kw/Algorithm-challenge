import sys
import heapq as hq

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x==0:
        if heap:
            print(hq.heappop(heap))
        else:
            print(0)
    else:
        hq.heappush(heap,x)