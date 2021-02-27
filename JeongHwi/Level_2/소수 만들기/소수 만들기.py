from itertools import combinations
from math import sqrt,ceil
def primes(n):
    primes = [True if i != 1 else False for i in range(n+1)]
    primes[0] = False
    primes[1] = False
    sq = ceil(sqrt(n))
    for i in range(2,sq+1):
        if primes[i]:
            for j in range(i+i,n+1,i):
                if not primes[j]:
                    continue
                primes[j] = False
    # print(primes)
    return primes
def solution(nums):
    nums.sort()
    pri = primes(sum(nums[-3:]))
    count = 0
    # print(pri)
    for x in combinations(nums,3):
        if pri[sum(x)]:
        #    print(x)
           count+=1
    return count
print(solution([1,2,3,4]))