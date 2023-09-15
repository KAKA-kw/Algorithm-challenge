# ✍DFS, BFS 알고리즘

## 💡그래프의 기본구조

![](https://velog.velcdn.com/images/hansoom3315/post/83096192-0afd-4ee2-9f9e-b62e105b462a/image.png)

- 노드와 간선으로 표현
- 그래프 탐색은 하나의 노드를 시작으로 다수의 노드를 방문

## 💡그래프의 표현방식

1. 인접행렬 : 2차원 배열로 그래프의 연결 관계를 표현한 방식
2. 인접리스트 : 리스트로 그래프의 연결관계를 표현한 방식

|     |  0  |  1   |  2   |
| :-: | :-: | :--: | :--: |
|  0  |  0  |  7   |  5   |
|  1  |  7  |  0   | 무한 |
|  2  |  5  | 무한 |  0   |

### 1. 인접행렬 방식

```python
graph = [ [0, 7 ,5], [7, 0, INF], [5, INF, 0] ]
```

=> 2차원 리스트로 표현
모든 관계를 저장하므로 노드 개수가 많을수록 메모리가 불필요하게 낭비된다

### 2. 인접리스트 방식

```python
graph = [[] for _ in range(3)]
# 노드 0에 연결된 노드 정보 저장
graph[0].append((1, 7))
graph[0].append((2, 5))
# 노드 1에 연결된 노드 정보 저장
graph[1].append((0, 7))
# 노드 2에 연결된 노드 정보 저장
graph[2].append((0, 5))
# graph =>
[[(1, 7), (2, 5)], [(0, 7)], [(0, 5)]]
```

=> 2차원 리스트로 표현
인접 행렬 방식에 비해 특정한 두 노드가 연결되어 있는 지에 대한 정보를 얻는 속도가 느리다

## 1. DFS 알고리즘

깊이 우선 탐색으로 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

> 스택과 재귀함수 개념을 활용하여 정의한다!

### 📖 DFS 예제

```python
def dfs(graph, v, visited):
	visited[v] = True
    for i in graph(v):
    	if not visited[i]:
        	dfs(graph, i, visited)
```

### 📖 예제1-음료수 얼려 먹기

> nxm 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 있는 부분은 1로 표시된다.  
> 얼음 틀 크기 정보를 입력을 받으면 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성해라

```python
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False
```

## 1. BFS 알고리즘

너비 우선 탐색으로 그래프에서 가까운 노드부터 탐색하는 알고리즘

> 큐 개념을 활용하여 정의한다!

### 📖 BFS 예제

```python
from collections from deque

def bfs(graph, start, visited):
	queue = deque([start])
    visited[start] = True
    while queue:
    	v = queue.popleft()
        for i in graph[v]:
        	if not visited[i]:
            	queue.append(i)
                visited[i] = True
```

### 📖 예제2-미로 탈출

> nxm 크기의 미로에 갇혀있다.
> 현재 위치는 (1,1)이며 미로의 출구는 (n, m)의 위치에 존재해 한 칸씩 이동할 수 있다. 괴물이 있는 부분은 0, 괴물이 없는 부분은 1로 표시되어 있다
> 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오

```python
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y= queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]
print(bfs(0, 0))
```

🧐 책 풀이와 같이 dx, dy리스트를 활용하여 네가지 방향의 위치에 대해서도 다 고려해야 한다!
