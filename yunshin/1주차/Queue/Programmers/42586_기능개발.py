# Queue
def solution(progresses, speeds):
    answer = []
    while progresses:
        for idx in range(len(speeds)): # 갱신
            progresses[idx] += speeds[idx]
        deploy = 0
        while progresses and progresses[0] >= 100:
            # 첫번쨰 기능이 100 이상이라면 배포
            # 그 다음 기능도 100 이상이라면 함께 배포.. 반복
            deploy +=1
            progresses.pop(0)
            speeds.pop(0)
        if deploy != 0:
            # 배포 갯수가 0개 인 날은 pass
            answer.append(deploy)
    return answer