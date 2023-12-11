def balanced_index(p):
    count = 0  # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':  # 왼쪽 괄호
            count += 1
        else:  # 오른쪽 괄호
            count -= 1
        if count == 0:  # 균형잡힌 괄호 문자열
            return i


def check_proper(p):
    count = 0  # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':  # 왼쪽 괄호
            count += 1
        else:  # 오른쪽 괄호
            if count == 0:  # 쌍이 맞지 않는 경우
                return False
            count -= 1
    return True  # 쌍이 맞는 경우


def solution(p):
    answer = ''
    if p == '':  # 빈 문자열인 경우
        return answer
    index = balanced_index(p)  # 균형잡힌 괄호 문자열 인덱스
    u = p[:index + 1]  # 균형잡힌 괄호 문자열
    v = p[index + 1:]  # 나머지 괄호 문자열
    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer
