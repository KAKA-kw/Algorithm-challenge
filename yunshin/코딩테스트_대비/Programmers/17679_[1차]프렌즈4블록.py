def check(m,n,x,y,graph):
    if(x+1<m and y+1<n):
        character = graph[x][y].split('*')[0]
        if((character in graph[x][y]) and   
           (character in graph[x+1][y]) and   
           (character in graph[x][y+1]) and   
           (character in graph[x+1][y+1])):
            return True
    return False

def reAlign(m,n,graph):
    for col in range(n):
        for row in range(m-1,-1,-1):
            tmpRow = row
            while(tmpRow!=-1 and graph[tmpRow][col]=='0'):
                tmpRow -= 1
            if(tmpRow!=row and tmpRow>=0):
                graph[row][col] = graph[tmpRow][col]
                graph[tmpRow][col] = '0'
            
def removeGroup(m,n,graph):
    for row in range(m):
        for col in range(n):
            if(graph[row][col]=='0'):
                continue
            if(check(m,n,row,col,graph)):
                graph[row][col]+='*'
                graph[row+1][col]+='*'
                graph[row][col+1]+='*'
                graph[row+1][col+1]+="*"
    flag = False          
    for row in range(m):
        for col in range(n):
            if("*" in graph[row][col]):
                flag = True
                graph[row][col] = '0'
    reAlign(m,n,graph)
    return flag

def solution(m, n, board):
    graph = [[] for _ in range(m)]
    for idx,row in enumerate(board):
        graph[idx] = list(row)
    
    removeRepeat = True
    while(removeRepeat):
        removeRepeat = removeGroup(m,n,graph)
    
    answer = 0
    
    for row in range(m):
        for col in range(n):
            if(graph[row][col]=='0'):
                answer+=1
    return answer