# 균형 잡은 괄호 문자열의 인덱스 반환
def balanced_index(p):
  cout = 0 # 왼쪽 괄호의 개수
  for i in range(len(p)):
    if p[i] == '(':
      count += 1
    else:
      count -= 1
    if count == 0:
      return i

# 올바른 괄호 문자열인지 판단
def check_proper(p):
  count = 0 # 왼쪽 괄호의 개수
  for i in p:
    if i == '(':
      count += 1
    else:
      if count == 0: # 쌍이 맞지 않는 경우
        return False
  return True

def solution(p):
  answer = ''
  if p == '':
    return answer
  index = balanced_index(p)
  u = p[:index+1]
  v = p[index+1:]
  if check_proper(u): # 올바른 괄호 문자열이면, v에 대해 함수를 수행한 결과를 붙여 반환
    answer = u + solution(v)

  #올바른 괄호 문자열이 아니라면 아래의 과정을 수행
  else:
    answer = '('
    answer += solution(v)
    answer += ')'
    u = list(u[1:-1]) # 첫 번째와 마지막 문자를 제거
    for i in range(len(u)):
      if u[i] == '(':
        u[i] = ')'
      else:
        u[i] = '('
    answer += "".join(u)
  return answer
