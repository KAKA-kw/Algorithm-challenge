def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1 # 시작 지점인 (1,1)에 1을 설정
    
    for i, j in puddles: 
        dp[j][i] = -1 # 물 웅덩이의 좌표를 찾아서 해당 좌표의 값을 -1로 설정
        
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1: 
                dp[i][j] = 0 # 물 웅덩이면 0으로 설정
                continue 
            # 왼쪽과 위쪽 좌표의 값을 더하여 현재 좌표에 저장
            dp[i][j] += (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
            
    return dp[n][m]
