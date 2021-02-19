def solution(s):
    answer = [0,0]
    while s != "1":
        temp = len(s)
        s = s.replace('0', '')
        temp -= len(s)
        s = format(len(s),'b')
        answer[0] += 1
        answer[1] += temp
    return answer

print(solution("110010101001"))