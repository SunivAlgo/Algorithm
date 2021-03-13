from collections import deque

def bfs(x, y, cnt, maps):
    mq = deque()
    n = len(maps[0])
    m = len(maps)
    mq.append((x, y, cnt))
    udlr = [[0,1], [0,-1], [1,0], [-1,0]]
    while mq:
        
        x, y, cnt = mq.popleft()

        for i in udlr:
            if x + i[0] >= n or x + i[0] < 0 or y + i[1] >= m or y + i[1] < 0:
                continue
            if x + i[0] == n - 1 and y + i[1] == m - 1:
                return cnt + 1
            elif maps[y + i[1]][x + i[0]] == 1:
                maps[y + i[1]][x + i[0]] = 0
                mq.append((x + i[0], y + i[1], cnt + 1))

    return -1

def solution(maps):
    maps[0][0] = 0
    return bfs(0, 0, 1, maps)

print(solution([
    [1,0,1,1,1],
    [1,0,1,0,1],
    [1,0,1,1,1],
    [1,1,1,0,1],
    [0,0,0,0,1]]))