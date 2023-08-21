# Hash
from collections import defaultdict

def solution(genres, plays):
    di1 = defaultdict(int)
    
    # di1 : key(장르) - value( 장르별 재생횟수 총합 )
    for idx in range(len(plays)):
        di1[genres[idx]] +=  plays[idx]
    
    sortedList = list(sorted(di1.items(), key=lambda x: -x[1]))
    # [('pop', 3100), ('classic', 1450)]
    
    # di2 : key(장르) - value( [(노래 재생횟수,노래 고유번호)....] )
    di2 = defaultdict(list)
    for idx in range(len(plays)):
        di2[genres[idx]].append((plays[idx],idx))
    for key in di2:
        di2[key].sort(key=lambda x: -x[0])
    # {'classic': [(800, 3), (500, 0), (150, 2)], 'pop': [(2500, 4), (600, 1)]})
    
    answer = []
    for genre,play in sortedList:
        answer.append(di2[genre][0][1])
        if len(di2[genre]) != 1:
            answer.append(di2[genre][1][1])
    return answer