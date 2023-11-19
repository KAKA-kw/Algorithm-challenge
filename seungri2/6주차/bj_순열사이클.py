t = int(input())  #테스트 케이스 수

def dfs(v):
  visited[v] = True #현재노드 방문으로 처리
  nv = graph[v] #인접노드
  
  #방문하지 않은 노드 dfs 함수 호출
  if not visited[nv]:
    dfs(nv)
  
for _ in range(t):
  n = int(input()) #순열 크기
  graph = list(map(int, input().split())) #순열 n개
  graph.insert(0, 0)  
  visited = [False] * (n + 1)
  cycle = 0  #순열 사이클 개수

  for i in range(1, n + 1):
    if not visited[i]: #방문X
      dfs(i) #함수 적용
      cycle += 1 #사이클 수 증가

print(cycle)