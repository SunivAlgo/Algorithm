def solution(n):
    ans = 1
    while n!=1:
        if n%2!=0: ans+=1
        n//=2
        
    return ans

#https://blog.naver.com/leemyo_/222259275192