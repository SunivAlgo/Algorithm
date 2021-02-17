def solution(land):
    for i in range(1, len(land)):
        for j in range(0, 4):
            m = 0
            for k in range(0, 4):
                if m < land[i-1][k] and k != j:
                    m = land[i-1][k]
            land[i][j] += m

    return max(land[-1])


land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))

'''
2번째 열부터 그 전의 행중에서 중복되지 않는행의 가장 큰수를 더해 준다.
끝까지 반복하면 마지막줄에 가장 큰 수가 답이 된다.
'''