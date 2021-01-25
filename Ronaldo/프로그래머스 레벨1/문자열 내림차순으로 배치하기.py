def solution(s):
    n = []
    answer = ''
    for i in range (0,len(s)):
        n.append(ord(s[i]))
    n.sort()
    n.reverse()
    for i in n:
        answer += chr(i)

    return answer