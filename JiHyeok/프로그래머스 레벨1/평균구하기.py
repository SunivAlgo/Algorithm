def solution(arr):
    answer = 0
    count = 0

    for i in arr :
        count += i
    answer = count / len(arr)
    return answer