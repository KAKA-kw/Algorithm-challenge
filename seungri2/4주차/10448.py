triangle = [n*(n+1)//2 for n in range(1,45)]
kaka = [0 for i in range (1001)]
for i in triangle:
    for j in triangle:
        for k in triangle:
            if i + j + k <= 1000:
                kaka[i+j+k] = 1
for i in range(int(input)):
    
    print(kaka[int(input())])