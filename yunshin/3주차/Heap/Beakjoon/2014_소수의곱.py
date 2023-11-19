# Heap
import sys
import heapq as hq

k,n = map(int,sys.stdin.readline().split())
initList = list(map(int, sys.stdin.readline().split()))
heap = []
for elem in initList:
    hq.heappush(heap,elem)
for _ in range(n-1):
    minNum = hq.heappop(heap)
    for elem in initList:
        hq.heappush(heap, elem*minNum)
        if minNum % elem ==0: # 자신을 포함하는 수까지만 heap 에 넣는다. ( 하나의 소수의 n 승으로 합성수를 만드는 것까지 허용 )
            break
print(hq.heappop(heap)) 