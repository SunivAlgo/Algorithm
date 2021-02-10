def solution(x):
    answer = True
    temp = x
    n = 0
    while(temp != 0):
        n += temp % 10
        temp = int( temp / 10)
    if(x % n != 0):
        answer = False

    return answer