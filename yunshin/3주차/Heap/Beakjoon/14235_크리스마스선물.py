# Heap
import sys
import heapq as hq

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    li = list(map(int,sys.stdin.readline().split()))
    if li[0] == 0: # 잼민이 만났을 때,
        if len(heap) == 0: # 줄게 없을 때,
            print(-1)
        else:
            print(-hq.heappop(heap))
    else: # 선물 충전소
        for i in range(li[0]):
            hq.heappush(heap,-li[i+1])