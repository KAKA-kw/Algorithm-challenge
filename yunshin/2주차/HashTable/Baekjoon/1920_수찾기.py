# Dictionary
import sys

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split(" ")))
m = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split(" ")))

di = {i: True for i in A} # A의 원소가 key, 값은 True 로 통일
for i in nums:
    if di.get(i,False): # nums 의 원소로 key 를 조회했을 때, 값이 없으면 False 반환
        print(1)
    else:
        print(0)