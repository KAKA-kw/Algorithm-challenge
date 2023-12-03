def solution(answers):
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    result = [0,0,0]
    for idx,ans in enumerate(answers):
        if ans == supo1[idx % 5]:
            result[0] += 1
        if ans == supo2[idx % 8]:
            result[1] += 1
        if ans == supo3[idx % 10]:
            result[2] += 1
            
    maxScore = max(result)
    answer = []
    for i in range(3):
        if result[i] == maxScore:
            answer.append(i+1)
    return answer