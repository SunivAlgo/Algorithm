from collections import deque

def solution(maps):
    q = deque()     # 큐에 시작지점의 위치, 깊이(cnt) 를 넣고 maps에서 해당위치 0으로 바꿔줌
    q.append([0, 0, 1])
    maps[0][0] = 0

    while q:    # q가 없어질때까지 bfs 반복
        y = q[0][0]     # q의 첫번째 요소의 위치, 깊이 를 가져옴
        x = q[0][1]
        cnt = q[0][2]
        if y == len(maps)-1 and x == len(maps[0])-1:    # 도착지점이면 종료
            return cnt
        
        q.popleft()     #요소를 가져온뒤 pop 하고 동서남북으로 maps에서 1로 존재하면 나아갈 위치를 q에 넣고 그 위치는 방문했으므로 0으로 바꿔줌
        if x < len(maps[0])-1 and maps[y][x+1] == 1:
            q.append([y, x+1, cnt+1])
            maps[y][x+1] = 0
        if x > 0 and maps[y][x-1] == 1:
            q.append([y, x-1, cnt+1])
            maps[y][x-1] = 0
        if y < len(maps)-1 and maps[y+1][x] == 1:
            q.append([y+1, x, cnt+1])
            maps[y+1][x] = 0
        if y > 0 and maps[y-1][x] == 1:
            q.append([y-1, x, cnt+1])
            maps[y-1][x] = 0
    
    return -1   #도착하지 못했을 경우 bfs 반복문을 통과 하게 됨

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	
print(solution(maps))

'''
처음에 dfs로 풀었으니 시간초과가 되어서 bfs를 알아 본 후 풀었다.
처음 bfs를 할때도 큐의 첫번째 요소를 pop하면서 maps[y][x] = 0 를 해주었는데 시간초과가 났다.
이 부분을 q에 넣을때 마다 해당 위치에 맞춰서 0으로 바꿔주니 시간초과가 나지 않았다. ex) maps[y][x+1] = 0
'''



'''answer = 100001

def dfs(maps, y, x, cnt):
    maps[y][x] = 0
    cnt += 1

    if y == len(maps)-1 and x == len(maps[0])-1:
        global answer
        if answer > cnt:
            answer = cnt
    
    if x < len(maps[0])-1 and maps[y][x+1] == 1:
        dfs(maps, y, x+1, cnt)
    if x > 0 and maps[y][x-1] == 1:
        dfs(maps, y, x-1, cnt)
    if y < len(maps)-1 and maps[y+1][x] == 1:
        dfs(maps, y+1, x, cnt)
    if y > 0 and maps[y-1][x] == 1:
        dfs(maps, y-1, x, cnt)

    maps[y][x] = 1

def solution(maps):
    dfs(maps, 0, 0, 0)
    if answer == 100001:
        return -1
    return answer
'''

