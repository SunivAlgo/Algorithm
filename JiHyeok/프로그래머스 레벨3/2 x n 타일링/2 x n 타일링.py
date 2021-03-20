
def solution(n):
    now = 3
    a,b = 1,2
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    while(now <= n):
        c = a + b
        a,b=b,c
        now += 1

    answer = c


    return answer % 1000000007

print(solution(4))
'''
    처음에 재귀로 구현했음 시간이 너무 오래 걸렸음.

    1.  규칙이 있을까 적어보니
    1 2 3 4 5 6  7  8
    1 2 3 5 8 13 21 34  
    순으로 진행됨.

'''
