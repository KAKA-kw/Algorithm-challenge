# 깊이 우선 탐색 (DFS - Depth First Search)

## 01 DFS의 특징:

1. **깊이 우선**: DFS는 한 경로를 최대한 깊게 탐색함. 즉, 한 분기점에서 모든 자식 노드를 탐색한 후 다음 형제 노드로 이동함.
2. **재귀 또는 스택**: DFS는 재귀 함수 또는 스택 자료구조를 사용하여 구현됨.
3. **백트래킹**: DFS는 특정 경로가 유효하지 않을 경우 백트래킹하여 이전 경로로 돌아감.

## 02 DFS의 구현:

- 주로 재귀 함수나 스택을 사용하여 DFS 구현 가능.

1. 재귀 함수를 사용한 구현:

```
def dfs(graph, node, visited):
    if node not in visited:
        print(node)  # 노드 방문 순서 출력
        visited.add(node)  # 노드를 방문 처리
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)  # 인접한 노드에 대해 재귀 호출
```

2. 스택을 사용한 구현:

```
def dfs(graph, start):
    visited = set()  # 방문한 노드를 저장하는 집합
    stack = [start]  # 스택 생성 및 시작 노드 추가

    while stack:
        node = stack.pop()  # 스택에서 노드 꺼내기
        if node not in visited:
            visited.add(node)  # 노드를 방문 처리
            print(node)  # 노드 방문 순서 출력
            neighbors = graph[node]  # 인접한 노드들 가져오기
            for neighbor in neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)  # 스택에 인접한 노드들 추가
```

## 03 DFS의 활용:

DFS는 주로 다음과 같은 상황에서 활용됨.

- **깊이 우선 탐색**: 그래프 또는 트리에서 모든 가능한 경로를 탐색하거나 특정 조건을 만족하는 경로를 찾을 때 사용됨.
- **백트래킹**: 조건을 만족하는 해를 찾거나 모든 조합을 탐색할 때 사용됨.
- **그래프의 연결성 확인**: 그래프 내에서 노드 간의 연결 여부를 확인하거나 사이클을 탐지할 때 사용됨.
