def solution(board):
    answer = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if i > 0 and j > 0 and board[i][j] == 1:
                board[i][j] = min([board[i-1][j], board[i][j-1], board[i-1][j-1]]) + 1
            if answer < board[i][j]:
                answer = board[i][j]
    if answer == 0:
        return 0
    return answer**2

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board))

'''
i 와 j가 0인 인덱스를 제외하고 1,1 인덱스 부터 끝까지 반복문을 시작한다
해당값이 1일 경우 오른쪽, 위쪽, 오르쪽위 대각선 값의 최소값을 찾아 +1
을 시킨값을 해당 인덱스 값으로 설정한다. DP 형식이다.
'''