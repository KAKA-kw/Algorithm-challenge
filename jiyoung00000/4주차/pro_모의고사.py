def solution(answers): # answers: 정답이 순서대로 들은 배열
    patterns = [
        [1, 2, 3, 4, 5], # 1번 수포자의 찍기 패턴
        [2, 1, 2, 3, 2, 4, 2, 5], # 2번 수포자의 찍기 패턴
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 3번 수포자의 찍기 패턴
    ]
    
    scores = [0, 0, 0] # scores: 수포자들의 점수
    
    for i, answer in enumerate(answers): # answers의 정답을 하나씩 반복
        for j, pattern in enumerate(patterns): # patterns의 찍기 패턴을 하나씩 반복
            if answer == pattern[i % len(pattern)]: # 정답과 찍기 패턴이 같은 경우
                scores[j] += 1 # 해당 수포자의 점수 1 증가

    max_score = max(scores) # max_score: 가장 높은 점수
    result = [i + 1 for i, score in enumerate(scores) if score == max_score] # result: 가장 높은 점수를 받은 수포자들의 번호  
    
    return result # result를 반환
