def solution(bridge_length, weight, truck_weights):
    answer = 0 # 총 걸린 시간을 저장하는 변수

    # 다리 위에 있는 트럭들을 나타내는 리스트
    trucks_on_bridge = [0] * bridge_length # 다리의 길이만큼의 공간을 가지며 초기값은 0으로 초기화
    while len(trucks_on_bridge): # 다리 위에 트럭이 있는 동안 반복
        answer += 1 # 시간 1초씩 증가
        trucks_on_bridge.pop(0) # 다리 위에서 가장 앞에 있는 트럭을 제거

        if truck_weights: # 남아있는 트럭이 있는 경우
            if sum(trucks_on_bridge) + truck_weights[0] <= weight: # 다리 위의 트럭 무게와 새로운 트럭의 무게를 합했을 때 다리가 견딜 수 있는 무게 이하라면
                trucks_on_bridge.append(truck_weights.pop(0)) # 새로운 트럭을 다리 위에 올림
            else: # 다리가 견딜 수 있는 무게를 초과한다면
                trucks_on_bridge.append(0) # 트럭 대신 0을 다리 위에 올림
    return answer # 총 걸린 시간 반환