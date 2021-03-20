def ton(now, n):
    if now == 0:
        return '0'
    answer = ''
    while now > 0 :
        r = now % n
        now = now // n
        if r >= 10:
            answer = str(chr(65 + r - 10)) + answer
        else:
            answer = str(r) + answer
    return answer

def solution(n, t, m, p):
    answer = ''
    cnt = 1
    now = 0
    if m == p:
        p = 0
    while len(answer) < t:
        strn = ton(now, n)

        for i in range(len(strn)):
            if cnt % m == p:
                answer = answer + strn[i]
            cnt += 1
            if len(answer) >= t:
                break
            
        now += 1
    return answer
print(solution(16, 16, 2, 2))
