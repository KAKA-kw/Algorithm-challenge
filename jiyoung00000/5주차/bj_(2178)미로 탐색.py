# BFS
# deque 사용
from collections import deque

# 상하좌우 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 입력 받기
N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

# BFS 함수 정의
def bfs():
    queue = deque()
    queue.append((0, 0))  # 시작 위치
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1

    while queue:
        x, y = queue.popleft()

        if x == N - 1 and y == M - 1:  # 도착 지점에 도달했을 때
            return visited[x][y]

        for i in range(4):  # 상하좌우 이동
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

# 최소 칸 수 출력
print(bfs())
