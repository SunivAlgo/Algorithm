from math import gcd
def solution(arr):
    lcm = arr[0]
    for i in range(1,len(arr)):
        gcd_number = gcd(lcm,arr[i])
        lcm = (lcm // gcd_number) * (arr[i] // gcd_number) * gcd_number
    answer = lcm
    return answer
print(solution([2,3,4]))
'''
    [a,b,c]라고 하면
    a,b의 최대공약수 g와 c의 최대공약수 gcd를 구하는 방식으로 해결하려 했음.
    반례 => [2,3,4]

    
    1.  a와 b의 최대공약수(g)를 구한다.
    
    2.  a * b / g = 최소공배수(l)
    
    3.  l 과 c의 최대공약수 (g)를 구한다.

    .
    .
    .
    .
    .(반복)


'''