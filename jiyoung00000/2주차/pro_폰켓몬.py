def solution(nums):
    pokemon_count = {} # 폰켓몬 종류를 저장할 해시 맵 생성
    
    for num in nums: # 폰켓몬 종류 개수 세기
        if num in pokemon_count:
            pokemon_count[num] += 1
        else:
            pokemon_count[num] = 1
    
    max_count = len(nums) // 2 # 고를 수 있는 폰켓몬의 최대 개수는 N/2

    unique_pokemon = len(pokemon_count) # 폰켓몬 종류의 개수
    
    # 만약 고를 수 있는 폰켓몬의 최대 개수가 폰켓몬 종류의 수보다 작다면,
    # 고를 수 있는 폰켓몬의 최대 개수를 반환, 아니면 폰켓몬 종류의 수를 반환
    return min(max_count, unique_pokemon)

# 간결한 풀이
# def solution(ls):
#    return min(len(ls)/2, len(set(ls)))
