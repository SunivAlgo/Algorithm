def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for i in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                answer[i][j]+=(arr1[i][k]*arr2[k][j])
    return answer

#https://blog.naver.com/leemyo_/222251644557