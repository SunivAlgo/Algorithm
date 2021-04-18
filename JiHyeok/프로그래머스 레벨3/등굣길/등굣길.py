def solution(m, n, puddles):
    answer = 0
    go_school_map = [[1] * m for _ in range(n)]

    for puddle in puddles:
        go_school_map[puddle[1]-1][puddle[0]-1] = 0
    
    for j in range(1, len(go_school_map[0])):
        if go_school_map[0][j-1] == 0:
            go_school_map[0][j] = 0
    
    for i in range(1, len(go_school_map)):
        if go_school_map[i-1][0] == 0:
            go_school_map[i][0] = 0
    
    for i in range(1,len(go_school_map)):
        for j in range(1, len(go_school_map[i])):
            if go_school_map[i][j] == 0: continue

            if go_school_map[i][j-1] == 0 and go_school_map[i-1][j] == 0:
                go_school_map[i][j] = 0
                continue

            if go_school_map[i][j-1] == 0 or go_school_map[i-1][j] == 0:
                if go_school_map[i][j-1] == 0 :
                    go_school_map[i][j] = go_school_map[i-1][j]
                else:
                    go_school_map[i][j] = go_school_map[i][j-1]
                continue

            go_school_map[i][j] = go_school_map[i][j-1] + go_school_map[i-1][j]


    

    answer = go_school_map[n-1][m-1]


    return answer % 1000000007
