mx = 1
def for_thefast(board,i,j):
    if i + mx > len(board)  or j + mx > len(board[i]) : return True
    '''
    for width in range(j,j+mx):
        if board[i][width] == 0:
            return True
    for height in range(i,i+mx):
        if board[height][j] == 0:
            return True
    '''
def width_is_one(board,h,w,width):
    for i in range(w,width + 1):
        if board[h][i] == 0 : break
    else : return True
    return False

def height_is_one(board,h,w,height):
    for i in range(h,height + 1):
        if board[i][w] == 0: break
    else : return True
    return False

def sol(board,i,j):
    global mx
    height = i + 1
    width = j + 1
    while height < len(board) and width < len(board[i]):
        if width_is_one(board,height,j,width) and height_is_one(board,i,width,height):
            if width - j + 1> mx:
                mx = width - j + 1
                
            height += 1
            width += 1
        else :
            break


def solution(board):
    answer = 1234
    global mx
    for i in board:
        if 1 in i:
            break
    else : return 0
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(len(board)):
        for j in range(len(board[i])):
            if for_thefast(board,i,j):
                continue
            if board[i][j] == 1:
                sol(board,i,j)

    return mx*mx

print(solution([[0,0,1,1],[1,1,1,1]]))

'''
    1.  2차원 리스트를 순회하면서, 1이 나타나면 그 자리에서 오른쪽,아래쪽으로 1의 개수를 세면서
        정사각형 판별 후 mx값 갱신
    
    2.  1000 *1000 개의 원소에 모두 계산을 해야해서 시간이 오래걸린다.
'''