# BFS
# deque 사용
from collections import deque 

def solution(begin, target, words): # begin: 시작 단어, target: 변환 단어, words: 단어의 집합
    if target not in words: # 변환할 수 없는 경우
        return 0 # 0 반환
    
    visited = set() # 방문한 단어들을 저장할 집합
    queue = deque([(begin, 0)]) # 시작 단어와 단계를 큐에 넣음

    while queue: # 큐가 빌 때까지 반복
        current_word, steps = queue.popleft() # 큐에서 원소를 하나 뽑아서 처리
        if current_word == target: # 변환할 수 있는 경우
            return steps # 단계 수 반환
        
        for word in words: # 단어 집합에 대해서
            if can_transform(current_word, word) and word not in visited: # 변환할 수 있고 방문하지 않은 경우
                visited.add(word) # 방문 표시
                queue.append((word, steps + 1)) # 큐에 추가
    
    return 0 # 변환할 수 없는 경우

def can_transform(word1, word2): # 두 단어가 변환 가능한지 여부를 반환
    diff_count = 0 # 다른 문자의 개수
    for i in range(len(word1)): # 두 단어에 대해서
        if word1[i] != word2[i]: # 다른 문자가 있으면
            diff_count += 1 # 다른 문자의 개수를 1 증가
        if diff_count > 1: # 다른 문자의 개수가 1보다 크면
            return False # 변환할 수 없음
    return diff_count == 1 # 다른 문자의 개수가 1이면 변환 가능
