def solution(arr1, arr2):
    answer = []

    for i in range(0,len(arr1)):
        answer.append([])
        for j in range(0,len(arr1[i])):
            
            answer[i].append(arr1[i][j] + arr2[i][j])
    return answer