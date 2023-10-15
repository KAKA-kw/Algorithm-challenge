def solution(N, number):
    # 가능한 숫자 표현을 저장할 DP 배열 초기화
    dp = [set() for _ in range(9)]
    
    # 초기값 설정
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
            
    # DP를 통해 가능한 숫자 표현 계산
    for i in range(1, 9):
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)
                        
        if number in dp[i]:
            return i
        
    return -1
