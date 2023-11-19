import heapq as hq

def solution(scoville, K):
    answer = 0
    # scoville 을 heap 구조로 바꿈
    hq.heapify(scoville)
    while True:
        # 가장 작은 값을 꺼낸다.
        minVal = hq.heappop(scoville)
        # 가장 작은 값이 K 이상이면 모든 값이 K 이상!
        if minVal >= K: 
            # 정답이 나옴, 반복문 탈출
            break
        # 가장 작은 값이 K 미만이면 두번째로 작은 값을 빼야하는데., 더이상 뺄값이 없다면
        elif len(scoville) == 0: 
            # 노답, 답 없음
            return -1
        # 두번째로 작은 값을 뺀다.
        secondVal = hq.heappop(scoville)
        # 첫번째로 뺀 값과 두번째로 뺀 값을 조합하여 새로운 값을 heap 에 넣음
        hq.heappush(scoville, minVal + secondVal*2)
        # 조합할 때마다, 횟수 갱신
        answer+=1
    return answer 