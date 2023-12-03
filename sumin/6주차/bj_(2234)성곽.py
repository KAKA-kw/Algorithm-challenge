# 런타임 에러(recursion error)때문에 추가(재귀 제한)
import sys

sys.setrecursionlimit(10000)

# 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기 못 풀었어요


n, m = map(int, input().split())
#n, m = 7, 4
# 방향 북:0 서:1 남:2 동:3
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 뚫려있는 방향을 리턴하는 함수
def find_direction(x):
    values = [1, 2, 4, 8]
    directions = [1, 0, 3, 2]
    answer = []
    for i in range(2**len(values)):
        # i를 j 만큼 오른쪽으로 시프트하고, & 1은 오른쪽에서 첫 번째 비트를 가져옴
        value = [values[j] for j in range(len(values)) if (i >> j) & 1]
        direction = [directions[j] for j in range(len(values)) if (i >> j) & 1]
        if sum(value) == x:
            return [d for d in directions if d not in direction]
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

#graph = [[11, 6, 11, 6, 3, 10, 6], [7, 9, 6, 13, 5, 15, 5], [1, 10, 12, 7, 13, 7, 5], [13, 11, 10, 8, 10, 12, 13]]
visited = [[False] * (n) for _ in range(m)]
counts = []
count = 0
def dfs(x, y):
    # 방 면적 계산
    global count
    # 방문한 적이 있는 경우
    if visited[x][y] == True:
        return False
    # 방문한 적이 없는 경우
    else:
        count += 1
        visited[x][y] = True
        if x >= 0 and y >= 0 and x < m and y < n:
            direction = find_direction(graph[x][y])
            for d in direction:
                nx = x + dx[d]
                ny = y + dy[d]
                if not visited[nx][ny]:
                    dfs(nx, ny)
        return True
# 방의 개수
answer = 0
for i in range(m):
    for j in range(n):
        if dfs(i, j):
            answer += 1
            # 방의 면적 리스트에 추가
            counts.append(count)
            # 방의 면적 다시 초기화
            count = 0
print(answer)
counts.sort()
print(counts[len(counts)-1])

