import heapq 
import sys

heap = [] # 힙 생성
N = int(sys.stdin.readline()) # 연산의 개수

for _ in range(N): # 연산의 개수만큼 반복
    x = int(sys.stdin.readline()) # 연산 입력 

    if x == 0: # x가 0이면
        if not heap: # heap이 비어있으면
            print(0) # 0 출력
        else: # heap이 비어있지 않으면
            print(-heapq.heappop(heap)) # 최대 힙이므로 음수로 저장된 값을 양수로 출력
    else: # x가 0이 아니면
        heapq.heappush(heap, -x) # 최대 힙이므로 음수로 저장