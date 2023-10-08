# 런타임 에러(recursion error)때문에 추가(재귀 제한)
import sys

sys.setrecursionlimit(10000)

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
# 영역 개수
answer = 0
# 영역 크기
counts = []
count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            # 영역이 있으면 1로 영역이 없으면 0으로
            if graph[j][i] == 0:
                graph[j][i] = 1
# DFS 으로 구현
def dfs(x, y):
    global count
    # 맵 안이면서 영역이 없는 경우
    if x >= 0 and y >= 0 and x < m and y < n and graph[x][y] == 0:
        graph[x][y] = 1
        count += 1
        # 4가지 방향으로 호출
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    else:
        return False

for i in range(m):
    for j in range(n):
        if dfs(i, j):
            answer += 1
            counts.append(count)
            count = 0

print(answer)
counts.sort()
print(" ".join(map(str, counts)))
