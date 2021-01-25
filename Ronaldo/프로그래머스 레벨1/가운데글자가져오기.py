def solution(s):
    length = len(s)
    answer = ''
    if length % 2 == 0:
        answer = s[length/2-1] + s[length/2]
    else:
        answer = s[(length-1)/2]
    return answer
