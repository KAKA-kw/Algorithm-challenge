# 오답 코드...

import heapq
import sys

K, N = map(int, sys.stdin.readline().split()) # K: 소수의 개수, N: 몇 번째인지
primes = list(map(int, sys.stdin.readline().split())) # 소수 리스트

result = 1 # N번째 소수의 곱
min_heap = [(result, 0)] # (소수의 곱, 소수 인덱스)

for _ in range(N):
    result, idx = heapq.heappop(min_heap) # 가장 작은 소수의 곱과 그 소수의 인덱스
    next_result = result * primes[idx] # 다음 소수의 곱
    heapq.heappush(min_heap, (next_result, idx)) # 다음 소수의 곱과 그 소수의 인덱스를 힙에 넣음
    
    # 중복 제거,,,
    if idx < K - 1: # 소수의 인덱스가 K - 1보다 작으면
        next_idx = idx + 1 # 다음 소수의 인덱스
        next_result = result * primes[next_idx] # 다음 소수의 곱
        heapq.heappush(min_heap, (next_result, next_idx)) # 다음 소수의 곱과 그 소수의 인덱스를 힙에 넣음

print(result) # N번째 소수의 곱 출력
