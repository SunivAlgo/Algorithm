
def solution(board):
    answer = 1234
    mx = 1
    for i in board:
        if 1 in i:
            break
    else: return 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == 0 or j == 0 or board[i][j] == 0 or board[i-1][j-1] == 0 or board[i-1][j] == 0 or board[i][j-1] == 0:
                continue
            else:
                a = board[i-1][j-1]
                b = board[i-1][j]
                c = board[i][j-1]
                m = min([a,b,c])
                board[i][j] = m + 1
                
                if board[i][j] > mx:
                    mx = board[i][j]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return mx*mx

print(solution([[0,0,1,1],[1,1,1,1]]))
'''
    풀이 참고하였음
    
    1.  정사각형이 되면 제일 오른쪽 아래에 정사각형의 변의 길이를 저장해 두는 방식

    2.  정사각형을 어떻게 판별하느냐

        1 1  >>  1 1
        1 1  >>  1 2

        에서 [0,0],[0,1],[1,0]의 값이 0이 아니어야 하고,
             [0,0],[0,1],[1,0]의 값중 최소값에 + 1 해준 값을 오른 쪽 아래에 저장한다.
'''