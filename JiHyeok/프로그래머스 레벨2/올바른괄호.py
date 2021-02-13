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

def solution(s):
    leftcount = 0
    rightcount = 0 
    answer = ''
    for i in range(0,len(s)):
        if s[i] == '(':
            leftcount += 1
        elif s[i] == ')':
            rightcount += 1
    
    if leftcount != rightcount :
        return False
    else :
        answer = is_right(s)

    print('Hello Python')

    return answer

print(solution("(()("))


'''
    괄호변환.py 의 올바른괄호문자열 판단 함수를 가져와 적용하였음
    
    1.  문자열에 '(' ')' 의 개수를 세어 개수가 다르면 일단 False return

    2.  개수가 같다면....
        a.  '(' ')' 의 개수를 세는 도중 ')'의 count가 '(' 보다 높게 올라가는 순간 잘못된 문자열이라고 판단
        b.  문자열 끝까지 ')'의 개수가 '(' 보다 같거나 작게 유지된다면 올바른 문자열
'''