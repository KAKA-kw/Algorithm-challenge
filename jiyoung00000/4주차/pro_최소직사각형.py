def solution(sizes): # sizes: 명함의 크기를 담은 2차원 배열
    answer = 0 # answer: 지갑의 최소 크기
    max_width = 0 # max_width: 명함의 가로 길이의 최댓값
    max_height = 0 # max_height: 명함의 세로 길이의 최댓값

    for size in sizes: # sizes의 명함의 크기를 하나씩 반복
        width, height = size # width: 명함의 가로 길이, height: 명함의 세로 길이
        max_width = max(max_width, max(width, height)) # max_width를 명함의 가로 길이와 세로 길이 중 최댓값으로 변경
        max_height = max(max_height, min(width, height)) # max_height를 명함의 가로 길이와 세로 길이 중 최솟값으로 변경
    
    answer = max_width * max_height # answer를 max_width와 max_height의 곱으로 변경
    return answer