# Stack
def solution(arr):
    stack = []
    for idx,ar in enumerate(arr):
        if idx == 0:
            stack.append(ar)
            continue
        if ar == stack[-1]:
            continue
        stack.append(ar)
    return stack