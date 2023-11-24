# dictionary

from collections import defaultdict

def compareDateDiff(dateNum1, todayDateNum):
    return dateNum1 <= todayDateNum
    
def parseDateNum(year, month, date):
    return (year*12*28)+(month*28)+date

def solution(today, terms, privacies):
    today_y,today_m,today_d = list(map(lambda x: int(x),today.split(".")))
    di = defaultdict()

    for term in terms:
        policy,deadline = term.split(" ")
        di[policy] = int(deadline)
    
    answer = []
    for idx,privacy in enumerate(privacies):
        join_ymd,join_p = privacy.split(" ")
        join_y,join_m,join_d = list(map(lambda x: int(x),join_ymd.split(".")))
        parseDateNum(join_y,join_m,join_d)
        if compareDateDiff(parseDateNum(join_y,join_m+di[join_p],join_d),parseDateNum(today_y,today_m,today_d)):
            answer.append(idx+1)
    
    return answer