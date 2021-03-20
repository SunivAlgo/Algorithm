def solution(n):
    answer = 0
    f = 1
    s = 2
    for i in range(2, n):
        answer = f + s 
        f = s
        s = answer    
    return answer % 1000000007

print(solution(4))