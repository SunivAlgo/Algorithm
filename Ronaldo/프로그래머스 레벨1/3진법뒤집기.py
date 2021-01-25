import math
def solution(n):
        
    
    answer = 0
    li = []
    while(n != 0):
        li.append(n % 3)
        n = int(n / 3)

    li.reverse()
    for i in range(0,len(li)):
        answer += int(li[i] * math.pow(3,i))
    return answer