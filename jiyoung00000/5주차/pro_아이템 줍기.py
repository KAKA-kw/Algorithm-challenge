# BFS
# deque 사용
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY): # rectangle: 직사각형의 좌표, characterX: 캐릭터의 초기 x좌표, characterY: 캐릭터의 초기 y좌표, itemX: 아이템의 x좌표, itemY: 아이템의 y좌표
    answer = 0 # 답
    
    characterX *= 2 # 캐릭터의 x좌표를 2배로
    characterY *= 2 # 캐릭터의 y좌표를 2배로
    itemX *= 2 # 아이템의 x좌표를 2배로
    itemY *= 2 # 아이템의 y좌표를 2배로
    
    max_x = max(characterX, itemX) + 2 # x좌표의 최댓값
    max_y = max(characterY, itemY) + 2 # y좌표의 최댓값
    field = [[-1] * max_y for _ in range(max_x)] # 필드
    
    for x1, y1, x2, y2 in rectangle: # 직사각형에 대해서
        for i in range(x1 * 2, x2 * 2 + 1): # 직사각형의 내부를 1로 표시
            field[i][y1 * 2] = 1 # 직사각형의 가장자리를 1로 표시
            field[i][y2 * 2] = 1 # 직사각형의 가장자리를 1로 표시
        for j in range(y1 * 2, y2 * 2 + 1): # 직사각형의 내부를 1로 표시
            field[x1 * 2][j] = 1 # 직사각형의 가장자리를 1로 표시
            field[x2 * 2][j] = 1 # 직사각형의 가장자리를 1로 표시
    
    dx = [-1, 1, 0, 0] # x좌표의 변화량
    dy = [0, 0, -1, 1] # y좌표의 변화량
    
    q = deque() # 큐
    q.append([characterX, characterY]) # 캐릭터의 초기 위치를 큐에 넣음
    
    while q: # 큐가 빌 때까지 반복
        size = len(q) # 큐의 크기
        for _ in range(size): # 큐의 크기만큼 반복
            x, y = q.popleft() # 큐에서 원소를 하나 뽑아서 처리
            
            # 도착 지점을 찾으면 종료 후 답을 반환
            if x == itemX and y == itemY: 
                return answer 
            
            for k in range(4): # 4방향에 대해서
                nx = x + dx[k] # 다음 x좌표
                ny = y + dy[k] # 다음 y좌표
                
                if 0 <= nx < max_x and 0 <= ny < max_y and field[nx][ny] == 1: # 범위 내에 있고, 직사각형의 가장자리인 경우
                    q.append([nx, ny]) # 큐에 추가
        
        answer += 1 # 답을 1 증가
    
    return 0  # 도달할 수 없는 경우
