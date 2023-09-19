# BFS
# deque 사용
# 최단 경로를 구해야 하는 경우 BFS를 이용하면 효과적
from collections import deque

def solution(maps):
    n = len(maps) # 행
    m = len(maps[0]) # 열
    dx = [-1, 1, 0, 0] # 좌우 방향
    dy = [0, 0, -1, 1] # 상하 방향
    
    # 시작 위치와 이동 거리를 큐에 넣음
    queue = deque() 
    queue.append((0, 0, 1))  # 시작 위치: (0, 0), 이동 거리: 1
    
    while queue: # 큐가 빌 때까지 반복
        x, y, dist = queue.popleft() # 큐에서 원소를 하나 뽑아서 처리
        
        # 상대 팀 진영에 도착한 경우
        if x == n - 1 and y == m - 1: # (n, m) 위치에 도착하면 종료
            return dist # 이동 거리 반환
        
        for i in range(4): # 상하좌우 4방향에 대해서
            nx = x + dx[i] # 다음 위치
            ny = y + dy[i] # 다음 위치
            
            # 다음 위치가 맵 내부이고 벽이 아니며, 방문하지 않은 곳이면 이동 가능
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1: # 맵 내부이고 벽이 아니며 방문하지 않은 곳이면
                queue.append((nx, ny, dist + 1)) # 큐에 추가
                maps[nx][ny] = 0  # 방문 표시로 벽을 0으로 변경
    
    # 상대 팀 진영에 도착할 수 없는 경우
    return -1 # -1 반환
