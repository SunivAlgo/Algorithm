def solution(m, n, puddles):
    answer = 0
    road = []
    for _ in range(n):
        road.append([0 for _ in range(m)])
    
    for puddle in puddles:
        road[puddle[1]-1][puddle[0]-1] = -1
    
    road[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if road[i][j] == -1:
                continue
            top = 0
            left = 0
            if i != 0 and road[i-1][j] != -1:
                top = road[i-1][j]
            if j != 0 and road[i][j-1] != -1: 
                left = road[i][j-1]
            road[i][j] += (top + left) % 1000000007
           
    return road[-1][-1]

print(solution(4,3,[[2, 2]]))
print(solution(4,3,[[1, 2]]))
#print(solution(100,100,[[2, 1]]))