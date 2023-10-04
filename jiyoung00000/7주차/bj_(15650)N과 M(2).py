# DFS_ backtracking
def dfs(N, M, depth, path, used): 
    if depth == M: # M개를 다 뽑았을 때
        print(" ".join(map(str, path))) # path를 출력
        return # 재귀 종료

    for i in range(1, N + 1): # 1부터 N까지
        if not used[i]: # i가 사용되지 않았으면
            # i와 같거나 작은 값을 사용함으로 표시
            for j in range(1, i + 1): 
              used[j] = True 
            path.append(i) # path에 i를 추가
            dfs(N, M, depth + 1, path, used) # depth를 1 증가시켜 재귀 호출
            path.pop() # path에서 i를 제거
            # i와 같거나 작은 값을 사용하지 않음으로 표시
            for j in range(1, i + 1):
              used[j] = False

N, M = map(int, input().split()) # N과 M을 입력받음
used = [False] * (N + 1) # 1부터 N까지 사용되었는지를 저장하는 배열
dfs(N, M, 0, [], used) # dfs 호출
