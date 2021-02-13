def solution(board):
    ylen = len(board)
    if ylen == 1:
        if 1 in board[0]:
            return 1
        else:
            return 0
    xlen = len(board[0])
    maxSize = -1
    for y in range(ylen):
        for x in range(xlen):
            if y == 0 or x == 0:
                continue
            if board[y][x] != 0:
                board[y][x] = min(board[y-1][x-1],board[y][x-1],board[y-1][x])+1
            maxSize = max(board[y][x],maxSize)
    for x in board:
        print(x)
    return maxSize**2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))