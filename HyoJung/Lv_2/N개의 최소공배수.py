from math import gcd

def solution(arr):
    tmp=1
    for num in arr:
        tmp= tmp*num//gcd(tmp,num)

    return tmp