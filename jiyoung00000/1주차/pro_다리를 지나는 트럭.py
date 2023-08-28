from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0 # 총 걸린 시간을 저장하는 변수
    trucks_on_bridge = deque() # 다리 위에 있는 트럭들을 나타내는 큐
    total_weight = 0 # 현재 다리 위에 있는 트럭들의 총 무게를 저장하는 변수

    while truck_weights or trucks_on_bridge:  # 아직 다리를 건너지 못한 트럭이나 다리 위에 트럭이 있는 경우
        answer += 1 # 시간 1초씩 증가

        if trucks_on_bridge: # 다리 위에 있는 트럭 중 가장 앞에 있는 트럭이 다리를 지났는지 확인
            if answer - trucks_on_bridge[0][1] >= bridge_length: # 다리를 지난 경우
                total_weight -= trucks_on_bridge.popleft()[0] # 다리를 지난 트럭을 큐에서 제거하고 총 무게에서 감소

        if truck_weights and total_weight + truck_weights[0] <= weight: # 새로운 트럭이 다리에 올라갈 수 있는지 확인
            truck = truck_weights.pop(0) # 다리에 올라갈 트럭을 큐에 추가하기 위해 리스트에서 제거
            trucks_on_bridge.append((truck, answer)) #  트럭과 진입 시간을 큐에 추가
            total_weight += truck # 총 무게에 추가된 트럭의 무게를 합산

    return answer # 총 걸린 시간 반환
