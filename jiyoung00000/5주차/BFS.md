# 넓이 우선 탐색(BFS_Breadth First Search)

## 01 덱의 특징:

1. **순서적 탐색**: 그래프나 트리와 같은 자료구조에서 노드를 순서대로 탐색하는 알고리즘.
2. **균일한 레벨**: 한 노드로부터 동일한 레벨에 있는 모든 노드를 먼저 방문한 후 다음 레벨로 이동.
3. **큐 (Queue) 사용**: 큐 자료구조를 활용하여 구현됨. 먼저 방문한 노드를 큐에 넣고, 큐에서 노드를 꺼내어 탐색을 진행함.

## 02 덱의 구현:

- 파이썬에서 collections 모듈의 deque 클래스를 사용하여 BFS 구현 가능.

```
from collections import deque

def bfs(graph, start):
    visited = set()  # 방문한 노드를 저장하는 집합
    queue = deque()  # 큐 생성
    queue.append(start)  # 시작 노드를 큐에 추가

    while queue:
        node = queue.popleft()  # 큐에서 노드 꺼내기
        if node not in visited:
            visited.add(node)  # 노드를 방문 처리
            print(node)  # 노드 방문 순서 출력
            neighbors = graph[node]  # 인접한 노드들 가져오기
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)  # 큐에 인접한 노드들 추가
```

## 03 덱의 활용:

BFS은 주로 다음과 같은 상황에서 활용됨.

- **최단 경로 탐색**: 시작점으로부터 목적지까지의 최단 경로를 찾을 때 사용됨.
- **그래프의 연결 여부 확인**: 그래프 내에서 두 노드 간의 연결 여부를 확인할 때 사용됨.
- **격자나 맵에서의 탐색**: 격자나 맵에서 특정 위치에서 시작하여 목표 위치까지의 최단 경로를 탐색할 때 활용됨.
