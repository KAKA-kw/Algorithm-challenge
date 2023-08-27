# deque 풀이
from collections import deque
import sys # input()보다 빠르게 입력받기 위함

n = int(sys.stdin.readline()) # 괄호의 수
deq = deque()

for i in range(n):
    words = sys.stdin.readline().split() # 문장을 단어로 나누기
    
    for word in words:
        if word != " ":
            deq.extend(word)
            while deq:
                print(deq.pop(), end="")
            print(" ", end="")