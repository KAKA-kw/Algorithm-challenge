def solution(brown, yellow):
    heights = []
    for h in range(1, brown//2):
        if h * ( (brown+4)//2 - h ) ==  brown+yellow:
            heights.append(h)
    if len(heights) == 1:
        return [heights[0],heights[0]]
    else:
        return sorted(heights,reverse=True)