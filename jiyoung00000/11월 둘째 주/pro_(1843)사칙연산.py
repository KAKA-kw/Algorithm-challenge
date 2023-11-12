def solution(arr):
    n = (len(arr) + 1) // 2  # 배열 arr의 길이에 따라서 n을 계산

    dp_max = [[-float('inf')] * n for _ in range(n)]  # 최댓값을 저장할 DP 테이블
    dp_min = [[float('inf')] * n for _ in range(n)]  # 최솟값을 저장할 DP 테이블

    # 초기값 설정
    for i in range(n):
        dp_max[i][i] = int(arr[i * 2])
        dp_min[i][i] = int(arr[i * 2])

    # DP 테이블 채우기
    for gap in range(1, n):
        for i in range(n - gap):
            j = i + gap
            for k in range(i, j):
                op = arr[k * 2 + 1]
                if op == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i]
                                       [k] + dp_max[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i]
                                       [k] + dp_min[k + 1][j])
                elif op == '-':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i]
                                       [k] - dp_min[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i]
                                       [k] - dp_max[k + 1][j])

    return dp_max[0][n - 1]  # 최종 결과는 0부터 n-1까지의 범위에서의 최댓값
