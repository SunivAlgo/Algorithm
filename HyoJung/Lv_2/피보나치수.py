def solution(n):
    a=0; b=1; f=0; cnt=2
    while(cnt<=n):
        f=(a+b)%1234567
        a=b; b=f; cnt+=1
    return f

#https://blog.naver.com/leemyo_/222247757396