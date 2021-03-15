def solution(m, n, board):
    answer = 0
    board = [list(s) for s in board]

    while(True):
        
        set_same_index = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != '*' and (board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]):
                    set_same_index.update([i * n + j , i * n + j + 1, (i + 1) * n + j, (i + 1) * n + j + 1])
        
        if not set_same_index:
            break
        list_same_index = sorted(list(set_same_index))
        answer += len(list_same_index)
        
        for i in list_same_index:
            if i < n:
                continue
            for k in range(i//n,-1,-1):
                if k == 0:
                    board[k][i%n] = '*'
                    break    
                board[k][i%n] = board[k - 1][i%n]

        ## print(board)
        ## print('\n')

        
        
                
    return answer

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))