from math import gcd
def lcm(a,b):
    return a*b//gcd(a,b)

def solution(arr):
    arrlen = len(arr)
    lcm_ = arr[0]
    for i in range(1,arrlen):
        lcm_ = lcm(lcm_,arr[i])
    return lcm_
        
print(solution([2,6,8,14]))
print(solution([1,2,3]))