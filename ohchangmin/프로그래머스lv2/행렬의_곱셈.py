def solution(arr1, arr2):
    answer = []
    for i in range(0, len(arr1)):
        add = []
        for j in range(0, len(arr2[0])):
            s = 0
            for k in range(0, len(arr2)):
                s += arr1[i][k] * arr2[k][j]
            add.append(s)
        answer.append(add)

    return answer
    
arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr1, arr2))

arr1 = [[1, 1, 1], [1, 1, 1]]
arr2 = [[1, 1], [1, 1], [1, 1]]
print(solution(arr1, arr2))
