# BFS 탐색으로 구현
from collections import deque

q = deque()
q.append((0, 0))

n, m = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
graph = []
for _ in range(n):
    str_graph = input()
    graph.append([int(x) for x in str_graph])

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 1:
            if nx != 0 or ny != 0:
              graph[nx][ny] = graph[x][y] + 1
              q.append((nx, ny))
    if graph[n-1][m-1] != 1:
        break

print(graph[n-1][m-1])