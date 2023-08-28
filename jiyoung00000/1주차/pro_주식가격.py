def solution(prices):
    length = len(prices) # 주식 가격의 길이를 저장하는 변수
    answer = [ i for i in range (length - 1, -1, -1)] # 주식 가격이 떨어지지 않은 기간을 저장하는 리스트
    
    stack = [0] # 주식 가격이 떨어지지 않은 기간을 저장하는 스택
    for i in range (1, length, 1): # 주식 가격의 길이만큼 반복
        while stack and prices[stack[-1]] > prices[i]: # 스택이 비어있지 않고, 스택의 마지막 원소가 현재 주식 가격보다 큰 경우
            j = stack.pop() # 스택의 마지막 원소를 꺼내서
            answer[j] = i - j # 현재 시간에서 스택의 마지막 원소의 시간을 뺀 값을 저장  
        stack.append(i) # 현재 시간을 스택에 추가
    return answer # 주식 가격이 떨어지지 않은 기간을 저장한 리스트 반환