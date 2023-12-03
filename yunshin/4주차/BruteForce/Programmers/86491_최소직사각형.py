def solution(sizes):
    # 큰 값을 가로로, 작은 값을 세로로
    maxWidth = -1
    maxHeight = -1
    for width,height in sizes:
        if width >= height:
            maxWidth = max(maxWidth,width)
            maxHeight = max(maxHeight,height)
        else:
            maxWidth = max(maxWidth,height)
            maxHeight = max(maxHeight,width)
            
    return (maxHeight*maxWidth)