def solution(priorities, location):
    # (인덱스, 우선순위) 튜플을 생성하여 큐를 구성
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0  # 출력된 프로세스의 수를 세는 변수를 초기화

    while True:
        cur = queue.pop(0) # 큐의 맨 앞에서 프로세스를 꺼내기

        # 큐에 남아있는 프로세스 중 현재 프로세스보다 우선순위가 높은 프로세스가 있는지 확인
        if any(cur[1] < q[1] for q in queue): # 우선순위가 높은 프로세스가 있다면 
            queue.append(cur) # 현재 프로세스를 큐의 맨 뒤에 다시 넣기
        else: # 현재 프로세스의 우선순위가 가장 높거나, 더 높은 우선순위 프로세스가 없을 경우
            answer += 1 # 출력된 프로세스의 수를 1 증가시킴

            # 현재 프로세스의 위치가 원하는 위치인지 확인
            if cur[0] == location:
                return answer  # 원하는 위치의 프로세스가 출력되었다면 해당 위치를 반환하고 종료

# any()
# 하나 이상의 인자를 받음.
# 인자로 받은 iterable(반복 가능한 객체) 중, 하나 이상의 요소가 True 값을 가지면 True를 반환
# 모든 요소가 False인 경우에는 False를 반환
