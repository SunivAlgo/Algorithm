def solution(arr1, arr2):
    answer = []
    len_arr1_row = len(arr1)
    len_arr1_column = len(arr1[0])
    len_arr2_row = len(arr2)
    len_arr2_column = len(arr2[0])
    
    for i in range(len_arr1_row):
        answer.append([0] * len_arr2_column)

    
    for i in range(len_arr1_row):
        for j in range(len_arr2_column):
            number = 0
            for k in range(len_arr1_column):
                number += arr1[i][k] * arr2[k][j]
            answer[i][j] = number

    return answer

print(solution([[1,4], [3,2], [4,1]],[[3, 3], [3, 3]]))

