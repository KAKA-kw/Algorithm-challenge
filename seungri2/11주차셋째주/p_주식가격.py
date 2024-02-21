def solution(prices):
    answer = [0]*len(prices)
    s = []
    
    for i, p in enumerate(prices):
        while s and prices[s[-1]] > p:
            j = s.pop()
            answer[j] = i-j            
        s.append(i)
    
    while s:
        i = s.pop()
        answer[i] = len(prices)-1-i
    
    return answer