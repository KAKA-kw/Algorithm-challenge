# DFS
# 재귀함수 사용
def solution(numbers, target): # DFS
    n = len(numbers) # numbers 길이
    answer = 0 # 정답
    def dfs(idx, result): # dfs 함수
        if idx == n: # 인덱스가 n과 같으면
            if result == target: # result가 target과 같으면
                nonlocal answer # answer 전역변수 사용
                answer += 1 # answer 증가
            return 
        else: # 인덱스가 n과 같지 않으면
            dfs(idx+1, result+numbers[idx]) # dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx]) # dfs(idx+1, result-numbers[idx])
    dfs(0,0) # dfs(0,0)
    return answer # 정답 반환