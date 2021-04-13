def solution(triangle):
    answer = 0

    for i in range(len(triangle)):
        if i == 0 : continue
        for j in range(len(triangle[i])):
            if j == 0: ## 삼각형의 왼쪽 변에 있는 값들은 위의 값을 그대로 물려받는다.
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1: ## 삼각형의 오른쪽 변에 있는 값들도 위의 값을 그대로 물려받는다.
                triangle[i][j] += triangle[i-1][j-1]
            else: ## 삼각형의 중앙에 있는 값들은 위의 두 값에서 값의 비교를 해서 큰값만 내려오게 한다.
                triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])
    answer = max(triangle[-1])
    print(triangle)
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))