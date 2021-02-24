from itertools import combinations

def isPrime(n):
    cnt=0
    for i in range(2, n):
        if n%i==0: cnt+=1
    
    if cnt==0: return True
    return False

def solution(nums):
    cnt=0
    sub_list= list(combinations(nums,3))     #Create sublist

    for i in sub_list:
        sub_sum=0
        for j in i: sub_sum+=j
        if isPrime(sub_sum): cnt+=1

    return cnt

#https://blog.naver.com/leemyo_/222255489473