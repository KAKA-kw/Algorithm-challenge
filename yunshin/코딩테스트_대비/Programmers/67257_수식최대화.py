from collections import defaultdict
from itertools import permutations

default_operator = ['+','-','*']

def calculation(oper,num1,num2):
    num1 = int(num1)
    num2 = int(num2)
    if(oper == "+"):
        return num1+num2
    if (oper == '-'):
        return num1-num2
    if (oper == '*'):
        return num1*num2

def getNextList(operation,expression_list):
    stack = []
    jump = False
    for idx in range(len(expression_list)):
        if(jump):
            jump = False
            continue
        if (expression_list[idx]==operation):
            stack.append(calculation(operation,stack.pop(),expression_list[idx+1]))
            jump = True
        else:
            stack.append(expression_list[idx])
    return stack
    

def solution(expression):
    #문자열을 배열로 바꾸기
    expression_list = []
    stack = [] 
    for ex in list(expression):
        if(ex in default_operator):
            expression_list.append(int("".join(stack)))
            expression_list.append(ex)
            stack = []
        else:
            stack.append(ex)
    expression_list.append("".join(stack))
    
    answer = -1
    for orderd_operations in permutations(default_operator,3):
        ex_list = expression_list.copy()
        for operation in orderd_operations:
            ex_list = getNextList(operation,ex_list)
        answer = max(answer, abs(ex_list[0]))
    return answer