# DFS
def dfs(graph, start, visited): 
    stack = [start]
    visited[start] = True # 방문 여부 True로 변경
    while stack: # stack이 빌 때까지 반복
        node = stack.pop() # stack에서 pop
        for neighbor in graph[node]: # node의 이웃들에 대해
            if not visited[neighbor]: # 방문하지 않았으면
                stack.append(neighbor) # stack에 추가
                visited[neighbor] = True # 방문 여부 True로 변경

def find_cycle_count(permutation): # 순열 사이클 개수 계산
    n = len(permutation) # 순열의 크기
    graph = [[] for _ in range(n)] # 그래프
    visited = [False] * n # 방문 여부
    cycle_count = 0 # 순열 사이클 개수

    for i in range(n): # 그래프 생성
        graph[i].append(permutation[i] - 1)  # 그래프에 간선 추가

    for i in range(n): 
        if not visited[i]: # 방문하지 않았으면
            dfs(graph, i, visited) # dfs 함수 호출
            cycle_count += 1 # 순열 사이클 개수 증가

    return cycle_count # 순열 사이클 개수 반환

# 테스트 케이스 수 입력
T = int(input())

for _ in range(T):
    # 순열의 크기 입력
    N = int(input())
    # 순열 입력
    permutation = list(map(int, input().split()))

    # 순열 사이클 개수 계산
    cycle_count = find_cycle_count(permutation)
    
    # 결과 출력
    print(cycle_count)
