from collections import deque

# BFS 활용
def solution(numbers, target):
    answer = 0
    q = deque()
    q.append([-numbers[0], 0, -numbers[0]])
    q.append([numbers[0], 0, numbers[0]])

    while q:
        num, idx, sum = q.popleft()
        if idx == len(numbers)-1:
            if sum == target:
                answer += 1
        if (idx + 1) < len(numbers):
            # 배열의 값 +, - 각각 큐에 넣기
            q.append([numbers[idx + 1], idx+1, sum+numbers[idx + 1]])
            q.append([-numbers[idx + 1], idx+1, sum-numbers[idx + 1]])
    return answer