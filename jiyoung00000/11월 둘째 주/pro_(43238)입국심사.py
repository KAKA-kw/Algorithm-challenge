def solution(n, times):
    start, end = 1, max(times) * n

    while start <= end:
        mid = (start + end) // 2
        count = 0

        # mid 시간 동안 각 심사관이 몇 명을 심사할 수 있는지 계산
        for t in times:
            count += mid // t

        # 심사할 수 있는 인원이 n보다 크거나 같으면 시간을 줄임
        if count >= n:
            end = mid - 1
        # 심사할 수 있는 인원이 n보다 작으면 시간을 늘림
        else:
            start = mid + 1

    return start
