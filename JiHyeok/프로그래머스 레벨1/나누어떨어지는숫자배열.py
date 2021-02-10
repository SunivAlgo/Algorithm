def solution(arr, divisor):
    answer = []
    count = -1
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            count += 1
    if count == -1:
        answer.append(-1)
    answer.sort()
    return answer
