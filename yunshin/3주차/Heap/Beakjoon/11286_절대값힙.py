import sys
import heapq as hq

heap = []
n = int(sys.stdin.readline())
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap:
            print(hq.heappop(heap)[1])
        else:
            print(0)
    else:
        if x<0:
            hq.heappush(heap,(-x,x))
        else:
            hq.heappush(heap,(x,x))
