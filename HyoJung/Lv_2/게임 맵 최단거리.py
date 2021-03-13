def solution(maps):
    queue = [[-1,-1],[0,0]]
    dir = [[0,-1],[-1,0],[0,1],[1,0]]
    visited = [[-1]*len(maps[0]) for i in range(len(maps))]
    visited[0][0]=0    

    while(True):
        tmp = queue.pop(1)
        i, j = tmp[0], tmp[1]
        for k in dir:
            x, y = i+k[0], j+k[1]
            if 0<=x and x<len(maps) and 0<=y and y<(len(maps[0])):
                if visited[x][y]==-1 and maps[x][y]!=0:
                    maps[x][y] = maps[i][j]+1
                    visited[x][y] = 0
                    queue.append([x,y])
        if maps[len(maps)-1][len(maps[0])-1]!=1: break
        if len(queue) == 1: break

    if maps[len(maps)-1][len(maps[0])-1]==1: return -1
    else: return maps[len(maps)-1][len(maps[0])-1]

# https://blog.naver.com/leemyo_/222273639450