import itertools # 순열을 구하기 위한 라이브러리

def is_prime(n): # 소수인지 판별하는 함수
    if n < 2: # 2보다 작은 경우
        return False # 소수가 아님
    if n == 2: # 2인 경우
        return True # 소수
    if n % 2 == 0: # 2로 나누어 떨어지는 경우
        return False # 소수가 아님
    for i in range(3, int(n ** 0.5) + 1, 2): # 3부터 n의 제곱근까지 홀수로 나누어 떨어지는지 확인
        if n % i == 0: # 나누어 떨어지는 경우
            return False # 소수가 아님
    return True # 소수

def solution(numbers): # numbers: 숫자로 이루어진 문자열
    answer = 0 # answer: 소수가 되는 숫자의 개수
    num_list = list(numbers) # num_list: numbers를 리스트로 변환한 값
    num_set = set() # num_set: numbers의 숫자로 만들 수 있는 모든 수의 집합
    
    for i in range(1, len(numbers) + 1): # numbers의 숫자로 만들 수 있는 모든 수를 구하기 위해 1부터 numbers의 길이까지 반복
        perms = itertools.permutations(num_list, i) # numbers의 숫자로 만들 수 있는 모든 수를 구함
        for perm in perms: # numbers의 숫자로 만들 수 있는 모든 수를 하나씩 반복
            num = int(''.join(perm)) # num: numbers의 숫자로 만들 수 있는 수
            num_set.add(num) # num_set에 num을 추가
    
    for num in num_set: # num_set의 숫자를 하나씩 반복
        if is_prime(num): # 소수인 경우
            answer += 1 # answer 1 증가
    
    return answer # answer를 반환