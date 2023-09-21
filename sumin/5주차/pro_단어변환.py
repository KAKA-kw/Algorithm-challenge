from collections import deque

# BFS 활용
def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    visited = [False] * len(words)
    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break        
        for i in range(len(words)):
            count = 0
            # 방문한 적이 없는 경우
            if not visited[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        count += 1
                # 글자 2개가 같은 경우 큐에 넣기
                if count == 1:
                    q.append([words[i], cnt+1])
                    visited[i] = True
                    
    return answer
