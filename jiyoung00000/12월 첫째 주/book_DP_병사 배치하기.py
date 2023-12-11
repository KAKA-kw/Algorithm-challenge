n = int(input())  # 병사 수
array = list(map(int, input().split()))  # 병사 정보
array.reverse()  # 순서 뒤집기

dp = [1] * n  # DP 테이블 초기화

for i in range(1, n):  # 2번째 병사부터
    for j in range(0, i):  # 0번째 병사부터 i-1번째 병사까지
        if array[j] < array[i]:  # 병사가 더 작은 경우
            dp[i] = max(dp[i], dp[j] + 1)  # dp[i] = dp[j] + 1
# 병사 최소 수 출력
print(n - max(dp))
