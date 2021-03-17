def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a = 1
        b = 2
        for i in range(3, n+1):
            if i % 2 == 1:
                a = (a + b) 
            else:
                b = (a + b) 
        return max([a,b]) % 1000000007

print(solution(6))

'''
피보나치로 풀었다.
'''