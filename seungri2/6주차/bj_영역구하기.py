import sys
sys.setrecursionlimit(10000)

def dfs(y, x, cnt):
    graph[y][x] = 1 #상하좌우로 이동해서 영역 크기 카운트
    for dy, dx in d:
        Y, X = y+dy, x+dx
        if (0 <= Y < M) and (0 <= X < N) and graph[Y][X] == 0:
            cnt = dfs(Y, X, cnt+1)
    return cnt
    
M, N, K = map(int, input().split()) #각각 행, 열, 직사각형 영역 개수
graph = [[0]*N for _ in range(M)] #리스트 생성해서 초기화
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1 #영역 정보 입력받고 1로 채우기
d = [(-1, 0), (1, 0), (0, -1), (0, 1)] #이동 방향 정의
res = [] #영역 크기 저장 리스트
for i in range(M): #배열 순회
    for j in range(N):
        if graph[i][j] == 0: #0인 영역에서 함수 호출해서 크기 계산
            res.append(dfs(i, j, 1))
print(len(res))
print(*sorted(res))