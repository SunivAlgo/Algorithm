import math
def solution(w,h):
    width = w
    height = h
    b = 0
    count = 0
    number = 2
    maxnumber = 1
    isPrime = 0

    if w == 1 or h == 1:
        return 0

    if w == h:
        return w * h - w

    if(w < h):
        temp = w
        w = h
        h = temp

    gradient = h/w
            
    for i in range(2,int(math.sqrt(w))):
        if w % i == 0:
            isPrime += 1
            break
    
    for i in range(2,int(math.sqrt(h))):
        if  h % i == 0:
            isPrime += 1
            break
    
    if isPrime >= 1:
        if w % h == 0:
            maxnumber *= h
            w = w // h
            h = h // h
        else :
            while True:
                if w % number == 0 and h % number == 0:
                    w = w // number
                    h = h // number
                    maxnumber *= number
                    number = 1
                number += 1
                if number > h//2:
                    break



    
    
    ''' for x in range(1,w+1):
        y = gradient * x
        count += 1
        if y - b > 1:
            count += 1
            b = int(y)
        
    '''## print("x:", x, " y:",y,' b',b," count:",count,)
    return width * height - (width + height - maxnumber)

print(solution(100000000,99999999))

'''
    내가 생각했던 방법
    1.  최대공약수를 구한다
    2.  width와 height를 최대공약수로 나눠준다
    3.  나눠진 width와 height에서 망가진 박스를 구하는데, 기울기 방정식을 구해가지고
        n번째 y 값과, n-1 번째 y값을 활용하여 구했음....
    4. 1문제 시간 초과.


    찾은 방법
    1.  최대공약수를 구한다.
    2.  N * M만큼의 사각형을 대각선으로 잘랐을 때 영향을 받는 사각형은 N + M -1이라는 것을 도출해야함.
'''