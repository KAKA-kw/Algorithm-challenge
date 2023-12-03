tests = int(input())
dp = []  # DP 테이블 초기화

for _ in range(tests):  # 테스트 케이스
    dp.append(list(map(int, input().split())))  # 정수 삼각형 정보
for i in range(1, n):  # 2번째 행부터
    for j in range(i + 1):  # 열
        if j == 0:  # 왼쪽 위에서 오는 경우
            left_up = 0  # 왼쪽 위가 없으므로 0
        else:  # 왼쪽 위에서 오는 경우
            left_up = dp[i - 1][j - 1]  # 왼쪽 위 값
        if j == i:  # 위에서 오는 경우
            up = 0  # 위가 없으므로 0
        else:  # 위에서 오는 경우
            up = dp[i - 1][j]  # 위 값
        dp[i][j] = dp[i][j] + max(left_up, up)  # 점화식
print(max(dp[n - 1]))  # 마지막 행의 최대값 출력
