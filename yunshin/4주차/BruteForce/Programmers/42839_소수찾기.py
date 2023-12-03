# DFS, 에라토스테네스의 체
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**(1/2))+1):
        if x%i == 0:
            return False
    return True

def solution(numbers):
    global numList, visited, numsSet
    numList = list(numbers)
    visited = [False] * len(numbers)
    numSet = set()
    def dfs(res):
        if len(res)<= len(numList):
            if res and res[0] =="0":
                return
            numSet.add(res)
        for i in range(len(numList)):
            if not visited[i]:
                visited[i] = True
                dfs(res + (numList[i]))
                visited[i] = False
    dfs("")
    answer = 0 
    numList = list(numSet)
    numList.remove("")
    for x in list(numList):
        if(isPrime(int(x))):
            answer+=1
    return answer