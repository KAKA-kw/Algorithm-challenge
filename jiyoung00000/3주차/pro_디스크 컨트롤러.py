import heapq

def solution(jobs):
    answer, current_time, i = 0, 0, 0 # answer: 평균 시간, current_time: 현재 시간, i: 처리한 작업의 개수
    start_time = -1 # 직전 작업이 끝난 시간
    job_heap = [] # 작업을 저장하는 우선순위 큐 

    # jobs를 요청 시간 기준으로 정렬
    while i < len(jobs): # 처리한 작업의 개수가 전체 작업의 개수보다 작은 동안 반복
        for job in jobs: # jobs의 작업을 하나씩 반복
            if start_time < job[0] <= current_time: # 작업의 요청 시간이 현재 시간보다 작고, 직전 작업이 끝난 시간보다 크거나 같은 경우
                heapq.heappush(job_heap, [job[1], job[0]]) # 작업을 job_heap에 추가

        if len(job_heap) > 0: # job_heap에 작업이 있는 경우
            current_job = heapq.heappop(job_heap) # job_heap에서 가장 소요 시간이 짧은 작업을 꺼냄
            start_time = current_time # 직전 작업이 끝난 시간을 현재 시간으로 변경
            current_time += current_job[0] # 현재 시간을 소요 시간만큼 증가
            answer += current_time - current_job[1] # answer에 현재 시간에서 작업의 요청 시간을 뺀 값을 더함
            i += 1 # 처리한 작업의 개수 1 증가
        else: # job_heap에 작업이 없는 경우
            current_time += 1 # 현재 시간 1 증가

    return answer // len(jobs) # answer를 작업의 개수로 나눈 몫을 반환
