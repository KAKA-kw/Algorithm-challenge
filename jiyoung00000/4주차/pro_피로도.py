from itertools import permutations # 순열을 구하기 위한 라이브러리

def solution(k, dungeons): # k: 체력, dungeons: 던전의 정보가 담긴 2차원 배열
    n = len(dungeons) # n: 던전의 개수
    max_dungeons = 0 # max_dungeons: 최대로 탐험할 수 있는 던전의 개수
    
    dungeon_order = list(range(n)) # dungeon_order: 던전의 순서를 담은 리스트
    for order in permutations(dungeon_order): # 던전의 순서를 하나씩 반복
        current_fatigue = k # current_fatigue: 현재 체력 
        explored_dungeons = 0 # explored_dungeons: 탐험한 던전의 개수

        for i in order: # 던전의 순서를 하나씩 반복
            min_required_fatigue, consumption = dungeons[i] # min_required_fatigue: 던전을 탐험하기 위해 필요한 최소 체력, consumption: 던전을 탐험하고 남은 체력
            if current_fatigue >= min_required_fatigue: # 현재 체력이 던전을 탐험하기 위해 필요한 최소 체력보다 크거나 같은 경우
                current_fatigue -= consumption # 현재 체력을 던전을 탐험하고 남은 체력만큼 감소
                explored_dungeons += 1 # 탐험한 던전의 개수 1 증가

        max_dungeons = max(max_dungeons, explored_dungeons) # max_dungeons를 탐험한 던전의 개수와 max_dungeons 중 최댓값으로 변경

    return max_dungeons # max_dungeons를 반환
