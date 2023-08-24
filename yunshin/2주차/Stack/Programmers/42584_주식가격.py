def solution(prices):
    answer = [i for i in range(len(prices)-1,-1,-1)] # 주식가격이 안떨어진다고 가정하고 초기화
    stack = []
    for idx,val in enumerate(prices):
        while stack and stack[-1][0] > val:
            preVal,preIdx = stack.pop()
            answer[preIdx] = idx-preIdx
        stack.append((val,idx))
    return answer