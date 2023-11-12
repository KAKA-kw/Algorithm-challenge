def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)  # 도착지점을 추가하여 계산을 용이하게 함
    start, end = 0, distance

    while start <= end:
        mid = (start + end) // 2
        min_distance = float('inf')
        current = 0
        remove_cnt = 0

        for rock in rocks:
            diff = rock - current
            if diff < mid:
                remove_cnt += 1
            else:
                current = rock
                min_distance = min(min_distance, diff)

        # 바위를 더 제거해야 함
        if remove_cnt > n:
            end = mid - 1
        # 바위를 더 제거하지 않아도 됨
        else:
            start = mid + 1
            answer = min_distance

    return answer
