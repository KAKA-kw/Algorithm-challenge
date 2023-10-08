# 시간 초과
def is_safe(board, row, col, N):
    # 같은 열에 다른 퀸이 있는지 확인
    for i in range(row):
        if board[i][col] == 1:
            return False

    # 왼쪽 위 대각선 방향 확인
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # 오른쪽 위 대각선 방향 확인
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queen(board, row, N):
    # 모든 퀸을 배치한 경우
    if row == N:
        return 1

    count = 0
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            count += solve_n_queen(board, row + 1, N)
            board[row][col] = 0  # 백트래킹

    return count

N = int(input())
board = [[0] * N for _ in range(N)]
result = solve_n_queen(board, 0, N)
print(result)
