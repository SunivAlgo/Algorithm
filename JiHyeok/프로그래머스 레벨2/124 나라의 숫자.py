def solution(n):
    answer = ''
    temp = n
    
    while n:
        if n % 3 != 0:
            answer = str(n % 3) + answer
            n = n // 3
        else :
            answer = '4' + answer
            n = n//3 - 1
    return answer

print(solution(12))



'''
    풀이 봤음
    1.  숫자가 3개밖에 없으므로 3진법을 적용한다고 생각 가능해야함.
    2.  3진법 계산하듯 하는데, 나머지가 0이면 4를 넣고 몫 -1
'''