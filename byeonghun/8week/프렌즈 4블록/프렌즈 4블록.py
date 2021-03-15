def removeBlock(m, n, board):
    check = [[False for _ in range(n)] for _ in range(m)]
    mark = 0
    for i in range(1, m):
        for j in range(1,n):
            if board[i-1][j] == board[i-1][j-1] == board[i][j-1] == board[i][j] and board[i][j] != '':
                check[i][j] = True
                check[i-1][j] = True
                check[i-1][j-1] = True
                check[i][j-1] = True

    for i in range(m):
        for j in range(n):
            if check[i][j] == True:
                board[i][j] = ''
                mark += 1

    if mark > 0:
        for i in range(n):
            top = -1
            for j in range(m - 1, -1, -1):
                if top == -1 and board[j][i] == '':
                    top = j
                    continue
                if top >= 0 and board[j][i] != '':
                    board[top][i] = board[j][i]
                    board[j][i] = ''
                    top -= 1 

    return board, mark


def solution(m, n, board):
    answer = 0
    for i in range(m):
        board[i] = list(board[i])
    while True:
        board, mark = removeBlock(m,n,board)
        if mark == 0:
            return answer
        else:
            answer += mark

    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))