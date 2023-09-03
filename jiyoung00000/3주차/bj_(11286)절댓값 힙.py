# (절댓값, 원래 값)의 튜플..?
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
            # 절댓값이 가장 작은 값을 출력하고 제거
            _, min_value = heapq.heappop(heap) 
            print(min_value) 
    else:
        heapq.heappush(heap, (abs(x), x)) # 절댓값, 원래 값의 튜플로 저장
        
# Comment: 최소힙이라서 절댓값이 같은 경우 작은 값부터 출력되는 듯..!
