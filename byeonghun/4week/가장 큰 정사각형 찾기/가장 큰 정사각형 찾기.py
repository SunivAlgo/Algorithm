import math

def isRectangle(board, row, col, size):
    for i in range(col, col + size):
        for j in range(row, row + size):
            if board[i][j] == 0:
                return False
    return True

def solution(board):
    x = len(board[0])
    y = len(board)
    size = x if x > y else y
    sumboard = 0
    for i in range(y):
        sumboard += sum(board[i])
    sumboard = math.floor(math.sqrt(sumboard))
    size = size if size < sumboard else sumboard
    while size > 0:
        for i in range(0, y - size + 1):
            for j in range(0, x - size + 1):
                if isRectangle(board, j, i, size):
                    return size * size
        size -= 1

    return size * size

print(solution([[1,1,1,1,0,0,0,0],
                [1,1,1,1,0,0,0,0],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1]]))