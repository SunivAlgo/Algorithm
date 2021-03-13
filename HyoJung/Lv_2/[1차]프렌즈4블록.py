def makeDown(m, n, board, visited):
    for j in range(n):
        s_block=[]
        for i in range(m):
            if visited[i][j]!=0 and board[i][j]!='-':
                s_block.append(board[i][j])
        i = m-1
        for k in range(len(s_block)):
            board[i][j]=s_block.pop(-1)
            i-=1
        while i>=0:
            if board[i][j]=='-': break
            board[i][j]='-'
            i-=1
    return board

def findSquare(m, n, board, visited, judge):
    for i in range(m-1,0,-1):
        for j in range(n-1,0,-1):
            s = board[i][j]
            if board[i][j-1]==s and board[i-1][j]==s and board[i-1][j-1]==s and s!='-':
                visited[i][j]=0; visited[i][j-1]=0
                visited[i-1][j]=0; visited[i-1][j-1]=0
                judge = True
    return visited, judge

def init(m,n,maps):
    visited = [[-1]*n for i in range(m)]
    board = [['']*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            board[i][j] = maps[i][j]
    return visited, board

def solution(m, n, maps):
    answer, judge = 0, False
    visited, board = init(m,n,maps)

    while(True):
        visited, judge = findSquare(m, n, board, visited, judge)
        if judge==False: break
        board = makeDown(m, n, board, visited)
        visited, judge = [[-1]*n for i in range(m)], False
    
    for i in board: answer+=i.count('-')
    return answer

# https://blog.naver.com/leemyo_/222274275063