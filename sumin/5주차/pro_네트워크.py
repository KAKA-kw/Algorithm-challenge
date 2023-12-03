# DFS 활용
def dfs(node, computers, visited, n):
  if visited[node] == False:
    # 방문 처리
    visited[node] = True
    for i in range(n):
      # 자기 자신이거나 방문한 적있으면 pass
      if node == i or visited[i] == True:
        continue
      if computers[node][i] == 1 and visited[i] == False:
        dfs(i, computers, visited, n)
    return True
  else:
    return False
  
def solution(n, computers):
  answer = 0
  visited = [False] * n

  for i in range(n):
    if dfs(i, computers, visited, n):
      answer += 1
  return answer