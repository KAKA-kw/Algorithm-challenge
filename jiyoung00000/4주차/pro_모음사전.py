from itertools import product # 중복순열
def solution(word): # word = 'AAAAE'
    alp = ['','A', 'E', 'I', 'O', 'U'] # 알파벳 리스트
    dict_words = list(product(alp, repeat=5)) # 중복순열로 알파벳 리스트에서 5개를 뽑아 만든 단어들의 리스트
    dict_list = [] # 단어들을 담을 리스트
    unique_list = [] # 중복을 제거한 단어들을 담을 리스트
    for dict_word in dict_words: # 단어들을 하나씩 꺼내서
        dict_list.append(''.join(dict_word)) # 단어를 만들어서 단어 리스트에 추가
    dict_list.sort() # 단어 리스트를 정렬
    [unique_list.append(x) for x in dict_list if x not in unique_list] # 중복을 제거한 단어들을 unique_list에 추가
    index = unique_list.index(word) # unique_list에서 word의 인덱스를 찾아서
    
    return index # 인덱스를 반환

# 배운 풀이
# def solution(word):
#    answer = 0
#    for i, n in enumerate(word):
#        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
#    return answer