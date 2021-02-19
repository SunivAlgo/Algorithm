def solution(land):
    answer = 0
    for i in range(len(land) - 1):
        col = 0
        max = 0
        for j in range(4):
            for k in range(4):
                if j == k: continue
                if land[i][j] + land[i][k] > max:
                    max = land[i][j] + land[i][k]
                    col = j
        land[i+1][col]
                
    return answer

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))