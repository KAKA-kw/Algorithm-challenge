import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())
    

while(T):
    h,l = map(int,input().split(" "))
    carPos = defaultdict(list)
    lastCar = 0
    
    for row in range(h):
        origin = list(map(int,input().split()))
        for col,car in enumerate(origin):
            if(car != -1) :
                carPos[car] = [row,col]
            lastCar = max(lastCar,car)
    
    result = 0
    curPossEachLayer = [0 for _ in range(h)]
    for car in range(1,lastCar+1):
        layer,idx = carPos[car]
        timeL = (layer)* 20
        timeC = min(abs(curPossEachLayer[layer]-idx), l - abs(curPossEachLayer[layer]-idx)) * 5
        curPossEachLayer[layer] = idx
        result += (timeL + timeC)
    print(result)    
    T-=1