def solution(s):
    answer=""
    for i, x in enumerate(s):
        if x==' ': answer+=" "
        elif i==0:
            if x.isalpha(): answer+=x.upper()
            else: answer+=x.lower()
        else:
            if x.isalpha() and s[i-1]==' ': answer+=x.upper()
            else: answer+=x.lower()
    return answer

#https://blog.naver.com/leemyo_/222254226959