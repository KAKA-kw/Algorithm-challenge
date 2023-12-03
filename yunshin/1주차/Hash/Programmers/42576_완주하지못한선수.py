# Hash
def solution(participant, completion):
    di = {name:0 for name in set(participant)}
    for name in participant:
        di[name]+=1
    for name in completion:
        di[name]-=1
    return [name[0] for name in di.items() if name[1]>0][0]