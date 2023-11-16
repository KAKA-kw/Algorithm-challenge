def getDiff(pos1,pos2):
    return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])
    
def solution(numbers, hand):
    di= {0:[3,1]}
    for i in range(0,9):
        di[i+1] = [i//3,i%3]    
    lHand = [3,0]
    rHand = [3,2]
    result = []
    for number in numbers:
        if(number==1 or number==4 or number==7):
            lHand = di[number]
            result.append("L")
            continue
        if(number==3 or number==6 or number==9):
            rHand = di[number]
            result.append("R")
            continue

        lDiff = getDiff(lHand,di[number])
        rDiff = getDiff(rHand,di[number])
        if(lDiff>rDiff):
            rHand = di[number]
            result.append("R")
        elif(lDiff<rDiff):
            lHand = di[number]
            result.append("L")
        else:
            if(hand=="left"):
                lHand = di[number]
                result.append("L")
            else:
                rHand = di[number]
                result.append("R")
    return "".join(result)