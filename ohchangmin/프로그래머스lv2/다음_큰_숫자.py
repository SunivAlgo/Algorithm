def solution(n):
    
    num = bin(n).count('1')
    answer = n+1
    while True:
        if num == bin(answer).count('1'):
            return answer
        answer += 1

n = 78
print(solution(n))

'''
bin, count 알아두기
'''