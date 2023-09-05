import heapq 

def solution(operations): 
    max_heap = [] # 최대 힙
    min_heap = [] # 최소 힙

    for operation in operations: # 연산 수행
        cmd, num = operation.split() # 명령어, 숫자 분리
        num = int(num) # 숫자는 정수형으로 변환
        
        if cmd == "I": # 삽입
            heapq.heappush(max_heap, -num) # 최대 힙에 삽입
            heapq.heappush(min_heap, num) # 최소 힙에 삽입
        elif cmd == "D" and num == 1: # 최대값 삭제
            if max_heap: # 최대 힙이 비어있지 않다면
                heapq.heappop(max_heap) # 최대 힙에서 최대값 삭제
                if len(max_heap) == 0 or -max_heap[0] < min_heap[0]: # 최대 힙이 비어있거나 최대 힙의 최대값이 최소 힙의 최소값보다 작다면
                    min_heap = [] # 최소 힙 초기화
                    max_heap = [] # 최대 힙 초기화
        elif cmd == "D" and num == -1: # 최소값 삭제
            if min_heap: # 최소 힙이 비어있지 않다면
                heapq.heappop(min_heap) # 최소 힙에서 최소값 삭제
                if len(min_heap) == 0 or -max_heap[0] < min_heap[0]: # 최소 힙이 비어있거나 최대 힙의 최대값이 최소 힙의 최소값보다 작다면
                    max_heap = [] # 최대 힙 초기화
                    min_heap = [] # 최소 힙 초기화 
                    
    if len(min_heap) == 0:
        return [0, 0]
    else:
        return [-max_heap[0], min_heap[0]] 
