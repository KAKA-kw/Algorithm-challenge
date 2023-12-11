tests = int(input())

for _ in range(tests):  # 테스트 케이스
    n, m = map(int, input().split())  # n: 행, m: 열
    array = list(map(int, input().split()))  # 금광 정보

    dp = []  # DP 테이블 초기화
    index = 0  # array 인덱스
    for i in range(n):  # 행
        dp.append(array[index:index+m])  # 열
        index += m  # m개씩 끊어서 넣기

    for j in range(1, m):  # 열
        for i in range(n):  # 행
            if i == 0:  # 왼쪽 위에서 오는 경우
                left_up = 0  # 왼쪽 위가 없으므로 0
            else:  # 왼쪽 위에서 오는 경우
                left_up = dp[i-1][j-1]  # 왼쪽 위 값
            if i == n-1:  # 왼쪽 아래에서 오는 경우
                left_down = 0  # 왼쪽 아래가 없으므로 0
            else:  # 왼쪽 아래에서 오는 경우
                left_down = dp[i+1][j-1]  # 왼쪽 아래 값

            left = dp[i][j-1]  # 왼쪽에서 오는 경우
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)  # 점화식

    result = 0  # 최대값 초기화
    for i in range(n):  # 행
        result = max(result, dp[i][m-1])  # 마지막 열의 값 중 최대값
    print(result)  # 결과 출력
