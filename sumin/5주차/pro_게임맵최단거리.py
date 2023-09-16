from collections import deque

# BFS 활용
def solutions(maps):
  answer = 0
  dx = [-1, 0, 1, 0]
  dy = [0, -1, 0, 1]

  n = len(maps)
  m = len(maps[0])

  q= deque()
  q.append((0,0))

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 맵 벗어나면 pass
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if maps[nx][ny] == 1:
        if nx != 0 or ny != 0:
          q.append((nx, ny))
          # 이동 => 기존 거리에 1 더하기
          maps[nx][ny] = maps[x][y] + 1
    if maps[n-1][m-1] != 1:
      break

  if maps[n-1][m-1] == 1:
    answer = -1
  else:
    answer = maps[n-1][m-1]
  return answer