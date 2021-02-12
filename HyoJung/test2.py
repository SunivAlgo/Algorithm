def solution(brown, yellow):
    div = []
    for i in range(1,yellow+1):     #약수구하기
        if yellow%i == 0: div.append(i)
            
    for i in range(0,len(div)+1):
        h = div[i]      #세로
        w = yellow/h    #가로
        if (w+2)*2 + h*2 == brown:
            answer = [w+2,h+2]
            return answer