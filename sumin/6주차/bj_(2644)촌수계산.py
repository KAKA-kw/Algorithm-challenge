# DFS로 구현
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
start, target = map(int, input().split())
m = int(input())
result = []
for _ in range(m):
    x, y= map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(x, depth):
    visited[x] = True
    if x == target:
        # target값과 동일할 때 촌수 result 리스트에 추가
        result.append(depth)
    for item in graph[x]:
        if not visited[item]:
            dfs(item, depth + 1)

dfs(start, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0])



