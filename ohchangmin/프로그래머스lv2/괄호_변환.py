def trueStr(p):
    st = []
    for i in p:
        if i == '(':
            st.append(i)
        elif i == ')':
            if len(st) == 0 or st[-1] != '(':
                return False
            else:
                st.pop()
    return True

def func(p):
    if p == '':
        return ''
    if trueStr(p):
        return p
    else:
        f = b = 0
        u = v = ""
        for i in range(0, len(p)):
            if p[i] == '(':
                f += 1
            else:
                b += 1
            u += p[i]
            if f == b:
                v = p[i+1:]
                break
        if trueStr(u):
            return u + func(v)
        else:
            s = '(' + func(v) + ')'
            u = u[1:len(u)-1]
            change_u = ""
            for i in range(0, len(u)):
                if u[i] == '(':
                    change_u += ')'
                else:
                    change_u += '('
            s += change_u
            return s

    
def solution(p):
    return func(p)

p = "()))((()"
print(solution(p))

'''
이 코드는 문제풀이 능력보다는 주어진 방식 그대로 구현할 수 있는
구현력만 있으면 되었다. 올바른 괄호 문자열은 스텍을 이용하여
짝이 맞는지 확인 하면 되었다.
'''