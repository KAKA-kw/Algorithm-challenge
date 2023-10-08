test = int(input())
result = []
def dfs(i, visited, array):
    if not visited[i]:
        visited[i] = True
        if not visited[array[i-1]]:
            dfs(array[i-1], visited, array)
  
for _ in range(test):
    answer = 0
    n = int(input())
    array = list(map(int, input().split()))
    visited = [False] * (len(array) + 1)

    for i in range(1, len(array) + 1):
        if not visited[i]:
            dfs(i, visited, array)
            answer += 1
    result.append(answer)

for r in result:
    print(r)
