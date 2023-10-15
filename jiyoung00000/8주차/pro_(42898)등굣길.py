
def solution(m, n, puddles):
    MOD = 1000000007

    # DP 테이블 초기화
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[1][1] = 1

    # 물에 잠긴 지역 표시
    for puddle in puddles:
        x, y = puddle
        dp[x][y] = -1

    # DP를 사용하여 최단 경로의 개수 계산
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue
            dp[i][j] += (dp[i - 1][j] + dp[i][j - 1]) % MOD

    return dp[m][n]
