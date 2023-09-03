import heapq
import sys

heap = [] # 힙 생성
N = int(sys.stdin.readline()) # 카드 묶음의 개수
sum_value = 0 # 최소 비교 횟수

for _ in range(N): # 카드 묶음의 개수만큼 반복
    x = int(sys.stdin.readline()) # 카드 묶음의 크기 입력
    heapq.heappush(heap, x) # 카드 묶음의 크기를 힙에 저장

while True: # 힙의 원소가 1개가 될 때까지 반복
    if len(heap) == 1:
        break
    min_value = heapq.heappop(heap)  # 가장 작은 카드 묶음을 꺼내기
    min_value += heapq.heappop(heap)  # 그 다음으로 작은 카드 묶음을 꺼내서 합치기
    sum_value += min_value  # 비교 횟수를 더하기
    heapq.heappush(heap, min_value)  # 합친 카드 묶음을 다시 힙에 넣기

print(sum_value) # 최소 비교 횟수 출력


