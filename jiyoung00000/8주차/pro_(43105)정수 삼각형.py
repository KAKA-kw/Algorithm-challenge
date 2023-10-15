def solution(triangle):
    # 삼각형의 높이
    n = len(triangle)
    
    # DP 테이블 초기화
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    
    # 다이나믹 프로그래밍을 사용하여 최댓값 계산
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0: # 외쪽 끝 요소
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j == i: # 오른쪽 끝 요소
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else: # 중간 요소
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
                
    # 마지막 행에서 최댓값 찾기
    answer = max(dp[n - 1])
    
    return answer