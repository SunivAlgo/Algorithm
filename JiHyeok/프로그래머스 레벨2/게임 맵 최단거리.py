from collections import deque
def play(start,maps):

    i = start[0]
    j = start[1]
    ori = new_map[i][j]
    new_map[i][j] = 0

    

    if i == end[0] and j == end[1]:
        switch = 0
        answer = min(ori, answer)
        return

    

def solution(maps):
    answer = 0
    for i in range(len(maps)):
        maps[i] = [0]+maps[i]+[0]
    maps = [[0]*len(maps[0])]+maps+[[0]*len(maps[0])]
    
    start = [1,1]
    end = [len(maps) - 2, len(maps[0]) - 2]

    i = start[0]
    j = start[1]

    q_for_bfs = deque()
    
    while i!= 0 and j!= 0:
        count = 0
        if maps[i - 1][j] == 1:
            q_for_bfs.append([i - 1 , j])
            count += 1

        if maps[i][j - 1] == 1:
            q_for_bfs.append([i , j - 1])
            count += 1

        if maps[i][j + 1] == 1:
            q_for_bfs.append([i , j + 1])
            count += 1

        if maps[i + 1][j] == 1:
            q_for_bfs.append([i + 1 , j])
            count += 1

        if not q_for_bfs:
            return -1

        for k in range(count):
            nxt = q_for_bfs.popleft()

        i = nxt[0]
        j = nxt[1]
        
        
        
    
    return answer
    
    
    

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))