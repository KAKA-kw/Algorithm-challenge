def solution(N, number):
    dp = [set() for i in range(9)]

    for i in range(1, 9):
        dp[i].add(int(str(N)*i))

        for j in range(i//2 + 1):
            for first in dp[j]:
                for second in dp[i-j]:
                    dp[i].add(first + second) # 덧셈 연산
                    dp[i].add(first - second) # 뺄셈 연산
                    dp[i].add(second - first) # 뺄셈 연산
                    dp[i].add(first * second) # 곱셈 연산
                    if second != 0 :
                        dp[i].add(first // second) # 나눗셈 연산
                    if first != 0 :
                        dp[i].add(second // first) # 나눗셈 연산
                    
        if number in dp[i]:
            return i
    return -1