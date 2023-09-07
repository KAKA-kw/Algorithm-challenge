from collections import deque 
def solution(n, wires):
    answer = []
    for expt in range(len(wires)):
        graph = [[False for _ in range(n+1)] for _ in range(n+2)]
        for i in range(len(wires)):
            if i == expt:
                continue
            graph[wires[i][0]][wires[i][1]] = True
            graph[wires[i][1]][wires[i][0]] = True
        
        # bfs
        q = deque()
        q.append(1)
        cnt = 0
        while q:
            curPos = q.popleft()
            cnt+=1
            for idx,val in enumerate(graph[curPos]):
                if val:
                    graph[curPos][idx] = False
                    graph[idx][curPos] = False
                    q.append(idx)
        answer.append(abs(n-2*cnt))
    return min(answer)
        