n = int (input())
array = []
for _ in range(n):
    colors = list(map(str, input()))
    array.append(colors)

maxCount = 0

def width():
    global maxCount

    for k in range(n):
        countRow = 1
        for l in range(n-1):
            if array[k][l] == array[k][l+1]:
                countRow += 1
                maxCount = max(maxCount, countRow)
            else:
                countRow = 1

def height():
    for k in range(n):
        global maxCount

        countColumn = 1
        for l in range(n-1):
            if array[l][k] == array[l +1][k]:
                countColumn += 1
                maxCount = max(maxCount, countColumn)

            else:
                countColumn = 1

for i in range(n):
    for j in range(n-1):
        if array[i][j] != array[i][j+1]:
            array[i][j], array[i][j+1] = array[i][j+1], array[i][j]
            width()
            height()
            array[i][j+1], array[i][j] = array[i][j], array[i][j+1]

        if array[j][i] != array[j+1][i]:
            array[j][i], array[j+1][i] = array[j+1][i], array[j][i]
            width()
            height()
            array[j+1][i], array[j][i] = array[j][i], array[j+1][i]

print(maxCount)