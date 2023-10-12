n,m= map(int,input().split())
s = []
 
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    #for 루프에서 1부터 n까지 반복하여 숫자를 s에 추가
    for i in range(1,n+1):
        s.append(i)
        dfs()
        s.pop()
dfs()