
def is_right(s): ## 올바른 문자열인지 확인하는 함수
    leftcount = 0
    rightcount = 0
    for i in s:
        if i == '(':
            leftcount += 1
        elif i == ')':
            rightcount += 1
        if rightcount > leftcount:
            break
    else : return True
    return False

def subtraction_reverse(s): ## 첫번째와 마지막 문자열을 제거하고 나머지 문자열의 괄호를 뒤집어 return하는 함수
    li_s = list(s)
    del(li_s[0])
    del(li_s[-1])
    s = ''.join(li_s)
    table = str.maketrans('()',')(')
    return s.translate(table)

def solution(p):
    leftcount = 0
    rightcount = 0 
    answer = ''
    if p == '': ## 빈 문자열 일때 빈 문자열return
        return p
    else :
        for i in range(0,len(p)):
            if p[i] == '(':
                leftcount += 1
            elif p[i] == ')':
                rightcount += 1
            if leftcount == rightcount : ## leftcount == rightcount 면 최소한의 균형잡힌 괄호 문자열
                left = p[0: i + 1]
                right = p[i + 1:]
                if is_right(left) == True : ## 올바른 문자열 일때
                    answer += p[0: i + 1]
                    answer += solution(right)
                    break
                elif is_right(left) == False : ## 균형잡힌 문자열 일때
                    answer += '('
                    answer += solution(right)
                    answer += ')'
                    answer += subtraction_reverse(left)
                    break
    return answer

print(solution("()))((()"))




'''
    1.  문제설명을 읽고 직관적으로 풀었음.
    2.  알고리즘 자체가 문제에 들어있음.
    3.  처음에 문자열을 나누는 기준만 언급하겠음.
        '(' 이면 leftcount + 1
        ')' 이면 rightcount + 1
        해줘서 leftcount == rightcount 가 되면 거기까지 균형잡힌 문자열이므로 U를 배정.
        V는 그 다음부터 문자열 끝까지 배정.
    4.  이 문제는 주석으로 요약.
'''