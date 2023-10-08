# 시간 초과
def is_valid(board, row, col, num):
    # 같은 행에 중복된 숫자가 있는지 검사
    if num in board[row]:
        return False
    
    # 같은 열에 중복된 숫자가 있는지 검사
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # 3x3 박스 내에 중복된 숫자가 있는지 검사
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # Backtrack
                return False
    return True

# 입력 받기
sudoku_board = []
for _ in range(9):
    row = list(map(int, input().split()))
    sudoku_board.append(row)

# 스도쿠 풀이 호출
solve_sudoku(sudoku_board)

# 결과 출력
for row in sudoku_board:
    print(*row)