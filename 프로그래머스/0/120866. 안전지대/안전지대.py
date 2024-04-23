def setD(board, temp_changes, i, j):
    if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] != 1:
        temp_changes.add((i, j))

def danger(board, a, b):
    if board[a][b] != 1:
        return

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    temp_changes = set()
    for dx, dy in directions:
        nx, ny = a + dx, b + dy
        setD(board, temp_changes, nx, ny)

    for (x, y) in temp_changes:
        board[x][y] = 2

def solution(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                danger(board, i, j)
    
    answer = 0
    for row in board:
        answer += row.count(0)
    return answer
