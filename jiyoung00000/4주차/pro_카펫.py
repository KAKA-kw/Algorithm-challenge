def solution(brown, yellow): # brown: 갈색 격자의 수, yellow: 노란색 격자의 수
    total = brown + yellow # total: 갈색 격자와 노란색 격자의 수의 합
    answer = [] # answer: 갈색 격자의 가로와 세로의 길이를 담을 리스트
    for width in range(1, int(total**0.5) + 1): # total의 제곱근까지 반복
        if total % width == 0: # total을 width로 나누어 떨어지는 경우
            height = total // width # height: total을 width로 나눈 몫
            if (width - 2) * (height - 2) == yellow: # 갈색 격자의 수에서 노란색 격자의 수를 뺀 값이 갈색 격자의 가로와 세로의 길이에서 2를 뺀 값의 곱과 같은 경우
                answer = [max(width, height), min(width, height)] # 갈색 격자의 가로와 세로의 길이를 반환
    return answer # answer를 반환