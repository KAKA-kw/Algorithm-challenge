def solution(board, moves):
    basket = []
    for col in moves:
        toy = -1
        for row in range(len(board)):
            if board[row][col-1] != 0:
                toy = board[row][col-1]
                board[row][col-1] = 0
                break
        if toy == -1:
            continue;
        basket.append(toy)
    
    answer = 0
    print(basket)
    stack = []
    for toy in basket:
        if(stack and stack[-1]==toy):
            stack.pop()
            answer += 2
        else:
            stack.append(toy)
    return (answer)