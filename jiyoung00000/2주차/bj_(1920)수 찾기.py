import sys # 시간 초과를 피하기 위해 sys 모듈 사용

N = int(sys.stdin.readline()) # N 입력 받기

keyList = list(map(int, sys.stdin.readline().split())) # 정수를 빠르게 검색하기 위해 리스트로 입력 받음

pool = {} # 정수를 빠르게 검색하기 위한 딕셔너리 생성
for k in keyList: # 딕셔너리에 정수들을 키로 저장
    pool[k] = 1 

M = int(sys.stdin.readline()) # M 입력 받기

target = list(map(int, sys.stdin.readline().split())) # 정수를 빠르게 검색하기 위해 리스트로 입력 받음

# 각각의 수에 대해 존재 여부를 출력
for t in target: # 리스트의 원소들을 하나씩 검색
    if t in pool: # 딕셔너리에 존재하는 경우
        sys.stdout.write("1\n")  # 1 출력
    else: # 딕셔너리에 존재하지 않는 경우
        sys.stdout.write("0\n")  # 0 출력
