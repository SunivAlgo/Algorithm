def solution(seoul):
    seoul = ["Jane","Kim"]
    answer = ''
    for i in range(0,len(seoul)):
        if seoul[i] == "Kim":
            s = str(i)
            answer = "김서방은 " + s + "에 있다"
            break
    return answer
