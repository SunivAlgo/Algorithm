def solution(s):
    answer = ''
    first = True
    for i in s:
        if first:
            if i >= 'a' and i <= 'z':
                answer += i.upper()
            else:
                answer += i
            first = False
        elif not first:
            answer += i.lower()
        if i == ' ':
            first = True

    return answer

s = "for the last week"
print(solution(s))

'''
first를 bool 값으로 주어 첫번쨰 글자 인지 판별하고 띄어쓰기가 나오면
first값을 바꿔주는 형식으로 s문자열을 한번 순회한다.
title() 함수 알아두기
'''