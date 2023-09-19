# DFS
def solution(n, computers): 
    answer = 0 # 정답
    visited = [False] * n # 방문 여부
    
    for i in range(n): # n번 반복
        if not visited[i]: # 방문하지 않았으면
            dfs(computers, visited, i) # dfs 함수 호출
            answer += 1 # 정답 증가
    
    return answer # 정답 반환


def dfs(computers, visited, node): # dfs 함수
    visited[node] = True # 방문 여부 True로 변경
    for i in range(len(computers)): # computers 길이만큼 반복
        if computers[node][i] == 1 and not visited[i]: # node와 i가 연결되어 있고 방문하지 않았으면
            dfs(computers, visited, i) # 재귀함수 호출

