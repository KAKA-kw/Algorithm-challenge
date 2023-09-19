# BFS
# deque 사용
from collections import deque # deque 사용
def solution(numbers, target): # BFS
    answer = 0 # 정답
    queue = deque() # 큐
    n = len(numbers) # numbers 길이
    queue.append([numbers[0],0]) # 큐에 [첫번째 수, 인덱스] 추가
    queue.append([-1 * numbers[0],0]) # 큐에 [-1 * 첫번째 수, 인덱스] 추가
    while queue: # 큐가 빌 때까지
        temp, idx = queue.popleft() # 큐에서 첫번째 원소를 빼서 temp, idx에 저장
        idx += 1 # 인덱스 증가
        if idx < n: # 인덱스가 n보다 작으면
            queue.append([temp+numbers[idx], idx]) # 큐에 [temp+numbers[idx], idx] 추가
            queue.append([temp-numbers[idx], idx]) # 큐에 [temp-numbers[idx], idx] 추가
        else: # 인덱스가 n보다 크거나 같으면
            if temp == target: # temp가 target과 같으면
                answer += 1 # 정답 증가
    return answer # 정답 반환