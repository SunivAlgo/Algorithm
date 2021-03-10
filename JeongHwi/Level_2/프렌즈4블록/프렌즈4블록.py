from collections import deque


def solution(m,n,board):
    board = [[x for x in board[i]] for i in range(m)]
    
    def check(y,x):
        nonlocal board
        nowBlock = board[y][x]
        st = [(y,x)]
        for dy,dx in [(0,1),(1,1),(1,0)]:
            if nowBlock == board[y+dy][x+dx]:
                st.append((y+dy,x+dx))
                continue
            else:
                st=[]
                return st
        return st

    def remove_Board(targets):
        nonlocal board
        for y,x in targets:
            board[y][x] = "X"

    def down_Block():
        nonlocal m,n,board
        for i in range(m-1,0,-1):
            for j in range(n):
                if board[i][j] == "X":
                    d = -1
                    while d+i>-1: 
                        if board[d+i][j] != "X":
                            board[i][j],board[d+i][j] = board[d+i][j],board[i][j]
                            break
                        d-=1
    
    count = 0
    while True:
        # CHECK
        targets=set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == "X":
                    continue
                sts = check(i,j)
                for s in sts:
                    targets.add(s)
        if not targets:
            return count
        count += len(targets)
        # REMOVE
        remove_Board(targets)
        # DOWN Block
        down_Block()
                

print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))