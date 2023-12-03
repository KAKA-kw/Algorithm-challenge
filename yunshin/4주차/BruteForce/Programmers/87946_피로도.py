# DFS
def solution(k, dungeons):
    global gDungeons, gResult, gVisited
    
    gDungeons = dungeons.copy()
    gResult = []
    gVisited = [False for _ in range(len(dungeons))]
    
    def dfs(cur,numExplore):
        gResult.append(numExplore)
        
        for i in range(len(dungeons)):
            if not gVisited[i]:
                if cur >= dungeons[i][0]:
                    gVisited[i] = True
                    dfs(cur-dungeons[i][1],numExplore+1)
                    gVisited[i] = False
    dfs(k,0)
    return max(gResult)
        