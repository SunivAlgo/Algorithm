import math

def solution(n, words):
    answer=[0, 0]

    for i, x in enumerate(words):
        if x in words[:i]:
            answer[0], answer[1] = i%n+1,math.ceil((i+1)/n)
            break  
        if i!=0:
            if x[0]!=words[i-1][-1]:
                answer[0], answer[1] = i%n+1, math.ceil((i+1)/n)
                break   
    return answer

#https://blog.naver.com/leemyo_/222255594925