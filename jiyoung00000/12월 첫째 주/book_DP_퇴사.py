n = int(input())
times = []
prices = []
dp = [0] * (n + 1)  # DP 테이블 초기화
max_value = 0  # 최대값 초기화

for _ in range(n):  # 테스트 케이스
    x, y = map(int, input().split())  # x: 상담 기간, y: 상담 금액
    times.append(x)  # 상담 기간
    prices.append(y)  # 상담 금액

for i in range(n - 1, -1, -1):  # 뒤에서부터 거꾸로 확인
    time = times[i] + i  # 현재 상담을 마치는 날짜
    if time <= n:  # 상담이 기간 안에 끝나는 경우
        dp[i] = max(prices[i] + dp[time], max_value)
        max_value = dp[i]
    else:  # 상담이 기간을 벗어나는 경우
        dp[i] = max_value
print(max_value)  # 최대값 출력
