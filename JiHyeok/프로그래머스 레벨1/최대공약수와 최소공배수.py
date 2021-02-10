def solution(n, m):
    answer = []
    temp = 0

    min = 1 # 최대공약수
    max = 1 # 최소공배수

    if(n > m):
        temp = n
        n =m
        m = temp

    a = n
    b = m
    c = 2

    while c <= a :
        if (a % c == 0) & (b % c == 0) :
            min *= c
            a = a / c
            b = b / c
        else :
            c += 1

    max = int(min * a * b)
    answer.append(min)
    answer.append(max)
    
    return answer