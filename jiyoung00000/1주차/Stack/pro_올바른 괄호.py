def solution(s):
    stack = [] # 괄호를 저장할 스택을 초기화
    
    for i in s: # 문자열 s를 순회
        if i == '(': # 왼쪽 괄호를 만나면            
            stack.append(i) # 스택에 추가
        
                # 오른쪽 괄호를 만났는데 스택이 비어있으면 올바르지 않은 괄호
        else: # 오른쪽 괄호를 만나면
            if stack == []: # 스택이 비어있으면
                return False # False를 반환하고 종료
            else: # 스택이 비어있지 않으면
                stack.pop() # 스택에서 가장 최근에 추가된 왼쪽 괄호를 제거

    if stack != []: # 문자열을 모두 순회한 뒤에도 스택에 왼쪽 괄호가 남아있으면
        return False # False를 반환하고 종료
    
    return True  # 모든 검사를 통과하면 올바른 괄호이므로 True를 반환
