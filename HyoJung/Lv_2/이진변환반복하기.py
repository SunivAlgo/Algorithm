def solution(s):
    answer=[0,0]
    while s!="1":
        answer[1]+=s.count("0")
        s=bin(len(s)-s.count("0"))[2:]
        answer[0]+=1
    return answer

#https://blog.naver.com/leemyo_/222247814044