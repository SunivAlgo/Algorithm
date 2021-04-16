def solution(m,n,puddles):
    maps = [[0 for _ in range(m)] for _ in range(n)]
    dp = [[0 for _ in range(m)] for _ in range(n)] # 각 칸은 해당 칸으로 갈 수 있는 방법의 개수
    for py,px in puddles:
        maps[px-1][py-1] = -1
    maps[n-1][m-1] = 2
    maps[0][0] = 1    

    for y in range(n):
        for x in range(m):
            if y==0 and x==0:
                dp[y][x] = 1
                continue
            if maps[y][x] == -1:
                continue
            up_y,up_x = y-1,x
            left_y,left_x = y,x-1
            
            # check 'up'
            if 0 <= up_y < n:
                dp[y][x] += dp[up_y][up_x]
            # check 'left'    
            if 0 <= left_x < m:
                dp[y][x] += dp[left_y][left_x]
    #print
    # for m in dp:
    #     print(m)
    return dp[n-1][m-1]%1000000007
print(solution(4,3,[[2,2]]))

"""
1  1  1  1
1  0  1  2
1  1  2  4

위 방법으로 보아
↑ 에 있는 방법 개수와, ← 에 있는 방법 개수를 더한다.

"""
