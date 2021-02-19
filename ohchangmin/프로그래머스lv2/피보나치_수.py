def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n+1):
            if i % 2 == 0:
                a = (a + b) 
            else:
                b = (a + b) 
        return max([a,b]) % 1234567

print(solution(4))