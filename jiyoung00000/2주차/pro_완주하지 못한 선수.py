def solution(participant, completion):
    participant_dict = {} # 빈 딕셔너리 생성
    
    for p in participant: # 참여자 명단을 딕셔너리에 이름을 키로, 참가 횟수를 값으로 저장
        if p in participant_dict:
            participant_dict[p] += 1
        else:
            participant_dict[p] = 1
    
    for c in completion: # 완주자 명단을 딕셔너리에서 참가 횟수를 감소시키며 제거
        participant_dict[c] -= 1
        if participant_dict[c] == 0:
            del participant_dict[c]

    answer = list(participant_dict.keys())[0] # 딕셔너리에 남아있는 선수가 완주하지 못한 선수
    
    return answer

# 간결한 풀이
# import collections

# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]