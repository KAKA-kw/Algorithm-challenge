N = int(input())
A, B = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)] # 노드들 간의 연결 관계
visited = [False] * (N+1) #방문 여부 & N+1로 크기 초기화
result = [] #최단거리 저장 리스트

# 연결된 노드들을 graph 배열에 저장
for _ in range(M):
  x, y = map(int, input().split())  
  graph[x].append(y)
  graph[y].append(x)

# 인접 노드 순회 & 방문 X 노드는 함수 호출
def dfs(v, num):
  num += 1
  visited[v] = True

  if v == B: #현재 노드 = B 이면 num 추가
    result.append(num)

  for i in graph[v]:
    if not visited[i]:
      dfs(i, num)

dfs(A, 0)
if len(result) == 0:
  print(-1)  #리스트 길이가 0 이면 이동 X -> -1 출력
else: #리스트 첫번째 요소에서 1 뺀값 출력 -> 최단거리 표시
  print(result[0]-1) 