from math import ceil

def solution(n,a,b):
    answer = 0

    while(a!=b):
      answer+=1
      a, b = ceil(a/2), ceil(b/2)
    
    return answer

# https://blog.naver.com/leemyo_/222258141522