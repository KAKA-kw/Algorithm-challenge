def solution(clothes):
    # 의상 종류별로 개수를 카운트
    clothes_dict = {}
    for cloth, cloth_type in clothes:
        if cloth_type in clothes_dict:
            clothes_dict[cloth_type] += 1
        else:
            clothes_dict[cloth_type] = 1

    # 모든 조합의 수 계산
    total_combinations = 1
    for count in clothes_dict.values(): # (각 종류별 의상 개수 + 1)을 모두 곱한 후, 모두 입지 않는 경우 1을 빼줌
        total_combinations *= (count + 1)

    return total_combinations - 1  # 모두 입지 않는 경우 1을 빼준 결과 반환
