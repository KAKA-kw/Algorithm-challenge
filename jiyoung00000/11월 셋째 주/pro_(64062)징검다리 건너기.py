# def solution(stones, k):  # 이분탐색
#     left, right = 1, max(stones)  # 최소 1명, 최대 가장 많은 사람이 건널 수 있는 경우

#     while left <= right:  # 이분탐색
#         mid = (left + right) // 2  # 건널 수 있는 사람의 수
#         count = 0  # 연속으로 못 건너는 돌의 개수
#         max_count = 0  # 최대 연속으로 못 건너는 돌의 개수

#         for stone in stones:  # 돌을 하나씩 확인
#             if stone - mid <= 0:  # 건널 수 있는 사람의 수보다 작거나 같으면
#                 count += 1  # 연속으로 못 건너는 돌의 개수 + 1
#             else:  # 건널 수 있는 사람의 수보다 크면
#                 max_count = max(max_count, count)  # 최대 연속으로 못 건너는 돌의 개수 갱신
#                 count = 0  # 연속으로 못 건너는 돌의 개수 초기화

#         # 마지막 돌까지 확인한 후 최대 연속으로 못 건너는 돌의 개수 갱신
#         max_count = max(max_count, count)

#         if max_count >= k:  # 최대 연속으로 못 건너는 돌의 개수가 k보다 크거나 같으면
#             right = mid - 1  # 건널 수 있는 사람의 수를 줄임
#         else:  # 최대 연속으로 못 건너는 돌의 개수가 k보다 작으면
#             left = mid + 1  # 건널 수 있는 사람의 수를 늘림

#     return left  # 최대 몇 명까지 건널 수 있는지 반환
def solution(stones, k): # 이분탐색
    left, right = 1, max(stones) # 최소 1명, 최대 가장 많은 사람이 건널 수 있는 경우

    while left <= right: # 이분탐색
        mid = (left + right) // 2 # 건널 수 있는 사람의 수
        cnt = 0  # 연속으로 못 건너는 돌의 개수
        flag = True  # 건널 수 있는지 없는지

        for stone in stones # 돌을 하나씩 확인:
            if stone < mid: # 건널 수 있는 사람의 수보다 작으면
                cnt += 1 # 연속으로 못 건너는 돌의 개수 + 1
                if cnt >= k: # 연속으로 못 건너는 돌의 개수가 k보다 크거나 같으면
                    flag = False # 건널 수 없음
                    break # 반복문 종료
            else: # 건널 수 있는 사람의 수보다 크면
                cnt = 0 # 연속으로 못 건너는 돌의 개수 초기화

        if flag: # 건널 수 있으면
            left = mid + 1 # 건널 수 있는 사람의 수를 늘림
        else:
            right = mid - 1 # 건널 수 있는 사람의 수를 줄임

    return left - 1 # 최대 몇 명까지 건널 수 있는지 반환
