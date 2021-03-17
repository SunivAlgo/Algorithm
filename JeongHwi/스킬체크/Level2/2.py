from itertools import combinations,permutations
import math
def getPrimes(maxNumber):
    # True is Prime
    primes = [True if i>1 else False for i in range(maxNumber+1)] 
    sq = math.ceil(math.sqrt(maxNumber))
    for i in range(2,sq):
        if primes[i]:
            for j in range(i+i,maxNumber+1,i):
                if not primes[j]:
                    continue
                primes[j] = False
    return primes


def solution(numbers):
    numbers = list(numbers)
    numlist = set()
    for i in range(1,len(numbers)+1):
        for x in permutations(numbers,i):
            numlist.add(int("".join(x)))
    # print(numlist)
    primes = getPrimes(max(numlist))
    count = 0
    for num in numlist:
        if primes[num] == True:
            count+=1
    return count

print(solution("17"))
print(solution("011"))