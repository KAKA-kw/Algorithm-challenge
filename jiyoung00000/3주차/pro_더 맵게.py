import heapq # 힙 모듈

def solution(scoville, K): 
    heapq.heapify(scoville)  # scoville 리스트를 최소 힙으로 변환
    mix_count = 0  # 섞은 횟수를 저장할 변수

    while scoville[0] < K: # scoville의 첫 번째 원소가 K보다 작은 동안 반복
        if len(scoville) < 2: # 음식이 2개 미만으로 남으면 모든 음식을 섞을 수 없으므로 -1 반환
            return -1  # 모든 음식을 K 이상으로 만들 수 없는 경우

        # 가장 맵지 않은 음식과 두 번째로 맵지 않은 음식을 꺼내서 섞음
        first = heapq.heappop(scoville) # 가장 맵지 않은 음식
        second = heapq.heappop(scoville) # 두 번째로 맵지 않은 음식
        new_scoville = first + (second * 2) # 섞은 음식의 스코빌 지수
        heapq.heappush(scoville, new_scoville) # 섞은 음식을 scoville에 추가
        mix_count += 1 # 섞은 횟수 1 증가

    return mix_count # 섞은 횟수 반환