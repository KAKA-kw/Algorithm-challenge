n,m = list(map(int,input().split()))
#n = 숫자 범위, m =  순열 길이
s = []

def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    #순열 길이 = m 이면 출력후 종료
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
    # 아니면, 1~n까지 s에 포함되지 않은 숫자 선택후 s에 추가
dfs()