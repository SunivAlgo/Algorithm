def solution(n):

    
    su = '수'
    bak = '박'
    answer = ''

    for i in range(0,n):
        if(i % 2 == 0):
            answer += su
        else:
            answer += bak

    return answer