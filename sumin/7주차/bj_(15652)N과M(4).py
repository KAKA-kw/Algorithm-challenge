n,m = map(int, input().split())

array = []

def dfs(start):
    if len(array)==m:
        print(' '.join(map(str,array)))
        return
    
    for i in range(start, n+1):
        array.append(i)
        dfs(i)
        array.pop()
    
dfs(1)