import sys

# y번째 열에서 n값이 가능한지 확인하는 함수
def check_col(n, y):
  for j in range(9):
    if n == graph[j][y]:
      return False
  return True

# x번째 행에서 n값이 가능한지 확인하는 함수
def check_row(n, x):
  for i in range(9):
    if n == graph[x][i]:
      return False
  return True

# (x, y)좌표를 포함하는 스도쿠 block안에 n값이 가능한지 확인하는 함수
def check_block(n, x, y):
  nx = x // 3 * 3
  ny = y // 3 * 3
  for i in range(nx , nx+3):
    for j in range(ny, ny+3):
      if graph[i][j] == n:
        return False
  return True

def dfs(count):
  # 스도쿠 0으로된 빈칸 다 채웠을 경우
  if count == len(check):
    # 스도쿠 다 print하고 함수 종료
    for i in range(9):
      print(*graph[i])
    exit()

  x = check[count][0]
  y = check[count][1]
  # 1부터 9까지 다 확인해서 맞는 숫자 찾기
  for i in range(10):
    if check_col(i, y) and check_row(i, x) and check_block(i, x, y):
      graph[x][y] = i
      dfs(count + 1)
      graph[x][y] = 0

graph = []
for i in range(9):
  graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 빈칸 (체크해봐야 하는 좌표들)
check = []

for i in range(9):
  for j in range(9):
    if graph[i][j] == 0:
      check.append([i, j])

dfs(0)
