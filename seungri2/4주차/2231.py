n = int (input())
result = 1000001

for i in range (1, n+1):
    sumTemp = list(map(int, str(i)))
    sumTemp.append(i)
    sumTemp = sum(sumTemp)

    if sumTemp == n:
        result = min(result, i)

if result < 1000001:
    print(result)
else:
    print(0)