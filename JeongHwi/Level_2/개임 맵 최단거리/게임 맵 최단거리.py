from collections import deque
def bfs(y,x,ylen,xlen,maps):
    q = deque([])
    q.append((y,x))
    visit = [[0 for _ in range(xlen)] for _ in range(ylen)]
    visit[0][0] = 1
    while q:
        now_y,now_x = q.popleft()
        for dy,dx in [(0,1),(1,0),(0,-1),(-1,0)]:
            ny,nx = now_y+dy,now_x+dx
            if 0<=ny<ylen and 0<=nx<xlen and visit[ny][nx] == 0 and maps[ny][nx] == 1:
                q.append((ny,nx))
                visit[ny][nx] = visit[now_y][now_x] + 1
                if ny == ylen-1 and nx == xlen-1:
                    return visit[ylen-1][xlen-1] # 도착했을 경우
    return -1 # 도착 못했을 경우 


def solution(maps):
    ylen = len(maps)
    xlen = len(maps[0])
    return bfs(0,0,ylen,xlen,maps)
    
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
