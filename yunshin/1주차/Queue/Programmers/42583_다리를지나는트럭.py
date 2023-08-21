#Queue
def solution(bridge_length, weight, truck_weights):
    # 다리에 하나의 트럭만 올릴 수 있는 경우
    if bridge_length == 1:
        return len(truck_weights)+1
    que = [0 for _ in range(bridge_length)] # 다리 위 진행 상황
    completed = [] # 다리를 완전히 지난 트럭 수
    totNum = len(truck_weights) # 지나가야할 트럭 수
    sumWeight = 0 # 다리 위에 있는 트럭 무게의 합
    answer = 0
    while len(completed) != totNum: # 지나간 트럭 수가 맨 처음 지나가야 했을 트럭 수와 같아지면 반복문 종료
        truck = que.pop(0) # 맨 앞에 거 (무게가 0 이면 빈공간, 아니면 트럭) 빠지고
        sumWeight -= truck
        if truck != 0: # 트럭이 빠진거면
            completed.append(truck) # complete 갱신

        if truck_weights and sumWeight+truck_weights[0] <= weight: # 다음 지나가야할 트럭이 있는 경우, 그 트럭의 무게와 다리 위의 트럭들 무게의 합을 weight 과 비교
            sumWeight += truck_weights[0]   # 다리 위, 트럭들의 무게 합을 갱신
            que.append(truck_weights.pop(0)) # 다리 위로 트럭 진입
        else:   # 지나가야할 트럭이 없거나, 다음 트럭이 들어왔을 때 무게가 초과된다면,
            que.append(0) # 트럭 진입 x, 다리 길이를 일정하게 유지하기 위해 0 삽입 
        answer+=1
    return answer