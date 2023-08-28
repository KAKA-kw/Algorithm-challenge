def solution(progresses, speeds):
    answer = []  # 각 기능이 배포될 때마다 몇 개의 기능이 함께 배포되는지를 저장하는 리스트
    day = 0  # 경과한 날짜를 나타내는 변수
    cnt = 0  # 하루에 배포되는 기능의 개수를 세는 변수
    
    while len(progresses) > 0:
        # 현재 기능의 진행도(progress)가 100% 이상인지 검사
        if (progresses[0] + day * speeds[0]) >= 100:
            progresses.pop(0)  # 진행된 기능 제거
            speeds.pop(0)  # 진행 속도 정보 제거
            cnt += 1  # 하루에 배포되는 기능 개수 증가
        else:
            if cnt > 0:
                answer.append(cnt)  # 배포할 기능 개수를 answer 리스트에 추가
                cnt = 0  # 기능 개수 초기화
            day += 1  # 날짜 증가 (기능이 하루씩 진행됨)
    
    answer.append(cnt)  # 마지막에 남은 기능들을 배포
    return answer  # 각 배포마다 함께 배포되는 기능의 개수를 담은 리스트 반환
