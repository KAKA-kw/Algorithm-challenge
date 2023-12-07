from functools import cmp_to_key
def solution(N, stages):
    
    # 분자: 실패한 사람수 , 분모: 도달한 사람 수, 인덱스
    fraction = [[0,0,i] for i in range(N+2)]
    for stage in stages:
        fraction[stage][0] +=1;    
    fraction[1][1] = len(stages)
    for i in range(2,N+1):
        fraction[i][1] = fraction[i-1][1] - fraction[i-1][0]
    fraction = list(filter(lambda x : x[2]!=0 and x[2]!=N+1,fraction))
    
    # 도달한 사람이 없는 경우 분모에 1, 분자에 0 을 주어 실패율 0으로 만듦
    for each in fraction:
        if(each[1]==0):
            each[0] = 0
            each[1] = 1
    
    answers = []
    def customSortCri(a,b):
        return b[0]/b[1] - a[0]/a[1] if a[0]/a[1] != b[0]/b[1] else a[2] - b[2]
    
    for _,_,answer in sorted(fraction,key = cmp_to_key(customSortCri)):
        answers.append(answer)
    return answers