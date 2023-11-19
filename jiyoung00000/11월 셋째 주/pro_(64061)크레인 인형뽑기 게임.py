def solution(board, moves):
    answer = 0
    basket = []

    for move in moves:
        column = move - 1  # moves의 값은 1부터 시작하지만, 리스트 인덱스는 0부터 시작하므로 1을 빼줌
        for i in range(len(board)):
            if board[i][column] != 0:  # 0이 아닌 첫 번째 인형을 찾음
                doll = board[i][column]
                board[i][column] = 0  # 인형을 집었으므로 해당 칸은 0으로 만듦

                if basket and basket[-1] == doll:
                    # 바구니의 가장 위에 있는 인형과 현재 집은 인형이 같으면 터트림
                    basket.pop()
                    answer += 2
                else:
                    # 같은 모양의 인형이 연속해서 쌓이지 않았을 경우 바구니에 추가
                    basket.append(doll)
                break

    return answer
