def solution(s, n):
    answer = ''
    answer = ''
    for i in range(0,len(s)):
        if s[i] != " ":
            if s[i].isupper() == False: # 소문자일때
                if (ord(s[i]) + n) > 122:
                    answer += (chr( ord(s[i]) + n - 26 ))
                else :
                    answer += (chr( ord(s[i]) + n ))
            else :
                if (ord(s[i]) + n) > 90:
                    answer +=  (chr( ord(s[i]) + n - 26 ))
                else :
                    answer += (chr( ord(s[i]) + n ))
        else :
            answer += " "
    return answer