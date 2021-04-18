def solution(m, n, puddles):
    answer = 0
    arr = [[0 for _ in range(m)] for _ in range(n)]
    for i in puddles:
        arr[i[1] - 1][i[0] - 1] = -1
    arr[0][0] = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == -1:
                continue
            if i + 1 != n and arr[i+1][j] != -1:
                arr[i+1][j] += arr[i][j]
            if j + 1 != m and arr[i][j+1] != -1:
                arr[i][j + 1] += arr[i][j]
    return arr[n - 1][m - 1] % 1000000007

print(solution(	4, 3, [[2, 2]]))