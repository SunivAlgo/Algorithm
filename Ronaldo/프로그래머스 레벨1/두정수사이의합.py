def solution(a, b):
    answer = 0
    temp = 0
    if a > b:
        temp = a
        a = b
        b = temp
    for i in range(int(a), int(b)+1):         # int를 붙여줘야하는 이유?
        answer += i
    return answer
