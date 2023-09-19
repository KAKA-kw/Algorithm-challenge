# BFS
# deque 사용
from collections import deque # deque 사용

def solution(n, computers): 
    answer = 0 # 정답
    visited = [False] * n # 방문 여부

    for i in range(n): # n번 반복
        if not visited[i]: # 방문하지 않았으면
            bfs(computers, visited, i) # bfs 함수 호출
            answer += 1 # 정답 증가

    return answer # 정답 반환


def bfs(computers, visited, node): # bfs 함수
    queue = deque() # 큐
    queue.append(node) # 큐에 node 추가
    visited[node] = True # 방문 여부 True로 변경

    while queue: # 큐가 빌 때까지
        current = queue.popleft() # 큐에서 첫번째 원소를 빼서 current에 저장
        for i in range(len(computers)): # computers 길이만큼 반복
            if computers[current][i] == 1 and not visited[i]: # current와 i가 연결되어 있고 방문하지 않았으면
                queue.append(i) # 큐에 i 추가
                visited[i] = True # 방문 여부 True로 변경