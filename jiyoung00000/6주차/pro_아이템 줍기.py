# BFS
# deque 사용
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0 # 답
    # 출발 지점과 도착 지점 좌표를 2배로 확장
    characterX *= 2 # 캐릭터의 x좌표를 2배로
    characterY *= 2 # 캐릭터의 y좌표를 2배로
    itemX *= 2 # 아이템의 x좌표를 2배로
    itemY *= 2 # 아이템의 y좌표를 2배로

    # 필드 크기를 변수로 설정
    field_size = 102

    # 필드를 -1로 초기화
    field = [[-1] * field_size for _ in range(field_size)]

    # 방문 여부를 저장하는 2D 배열 초기화
    visited = [[1] * field_size for _ in range(field_size)]
    visited[characterX][characterY] = 0

    # 직사각형 영역을 표시
    for r in rectangle:
        x1, y1, x2, y2 = r
        x1 *= 2
        y1 *= 2
        x2 *= 2
        y2 *= 2
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                elif field[i][j] != 0:
                    field[i][j] = 1
    
    dx = [-1, 1, 0, 0] # x좌표의 변화량
    dy = [0, 0, -1, 1] # y좌표의 변화량
    
    q = deque() # 큐
    q.append([characterX, characterY]) # 캐릭터의 초기 위치를 큐에 넣음
    
    while q: # 큐가 빌 때까지 반복
        x, y = q.popleft() # 큐에서 원소를 하나 뽑아서 처리
        # 도착 지점을 찾으면 종료 후 답을 반환
        if x == itemX and y == itemY:
            answer = visited[x][y] // 2
            break
        
        # 상하좌우 탐색
        for k in range(4): # 4방향에 대해서
            nx = x + dx[k] # 다음 x좌표
            ny = y + dy[k] # 다음 y좌표
            # 필드를 벗어나지 않고, 방문하지 않았으며, 직사각형 영역이 아니면 큐에 추가
            if 0 <= nx < field_size and 0 <= ny < field_size and field[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append([nx, ny]) # 큐에 추가
                visited[nx][ny] = visited[x][y] + 1

    return answer
