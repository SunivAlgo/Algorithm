

def solution(n):
    answer = ''

    while n > 0:
        a = str(n%3)
        answer = a + answer
        n/=3
        n = int(n)
        if a == "0":
            n -= 1

    return answer.replace('0','4')

"""
n을 3으로 나눈 나머지를 문자열에 더한다.
n을 3으로 나눈다.
n을 3으로 나눈 나머지가 0 이면 n에 1을 뺀다.
(이 부분은 생각했다기 보단 1 ~ 10까지 값을 넣어보면서 찾은 것이다)
마지막에 문자열에서 0은 4로 바꾸고 마무리 한다
"""