# 실패 코드..
# 테스트 1
# 입력값 〉	["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
# 기댓값 〉	[0, 0]
# 실행 결과 〉	실행한 결괏값 [123,123]이 기댓값 [0,0]과 다릅니다.
import heapq

def solution(operations):
    max_heap = [] 
    min_heap = [] 

    for operation in operations:
        cmd, num = operation.split()
        num = int(num)
        
        if cmd == "I": 
            heapq.heappush(max_heap, -num) 
            heapq.heappush(min_heap, num) 
        elif cmd == "D" and num == 1: 
            if max_heap: 
                heapq.heappop(max_heap) 
        elif cmd == "D" and num == -1: 
            if min_heap: 
                heapq.heappop(min_heap) 

    if not max_heap or not min_heap: 
        return [0, 0]
    else:
        return [-max_heap[0], min_heap[0]] 
