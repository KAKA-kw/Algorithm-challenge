# Queue
def solution(priorities, location):
    que = [(val,idx) for idx,val in enumerate(priorities)]
    silhang = 0
    while que:
        Priority = max(priorities)
        deagi = que.pop(0)
        if deagi[0] == Priority:
            silhang+=1
            if deagi[1] == location:
                return silhang
            priorities.remove(Priority)
            continue
        else:
            que.append(deagi)