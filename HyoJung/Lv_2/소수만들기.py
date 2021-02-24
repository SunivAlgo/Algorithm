from itertools import combinations

def isPrime(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True

def solution(nums):
    cnt=0
    sub_list= list(combinations(nums,3))     #Create sublist

    for i in sub_list:
        if isPrime(sum(i)): cnt+=1
    return cnt

#https://blog.naver.com/leemyo_/222255489473