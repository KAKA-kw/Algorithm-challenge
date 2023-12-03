def solution(word):
    # global candidate,dictionary
    candidate = ['A','E','I','O','U']
    dictionary = []
    def dfs(subStr):
        if len(subStr) > 5:
            return
        else:
            if len(subStr) != 0:
                dictionary.append(subStr) 
        for can in candidate:
            dfs(subStr+can)
    dfs("")
    def customSort(x):
        for i in range(5):
            return x[i]
    dictionary.sort(key = customSort)
    answer = 0
    for el in dictionary:
        if el == word:
            return answer+1
        answer+=1