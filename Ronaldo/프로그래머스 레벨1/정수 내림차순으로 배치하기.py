import math
def solution(n):
    number = []
    answer = 0
    while n != 0 :
        number.append(n % 10)
        n = int(n / 10)
    number.sort()
    for i in range (0,len(number)):
        answer += int(number[i] * math.pow(10 , i))
    
    return answer