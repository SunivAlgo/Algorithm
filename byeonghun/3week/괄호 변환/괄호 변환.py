def isright(p): # -1 이면 오히려 맞는거
    stack = []
    for v in p:
        if not stack:
            stack.append(v)
            continue
        if v == ')':
            if stack[-1] == '(': # ()
                stack.pop()
            else: #))
                stack.append(v)
        else:
            if stack[-1] == '(': # ((
                stack.append(v)
            else : # )(
                return False
    return True

def splitp(u):
    d = {'(' : 0, ')' : 0}
    for i, v in enumerate(u):
        if v == '(': d['('] += 1
        else : d[')'] += 1
        if d['('] == d[')']:
            return u[:i + 1], u[i + 1:]
    
def reversedu(u):
    temp = ''
    for i in range(1, len(u) -1):
        if u[i] == '(':
            temp += ')'
        else :
            temp += '('
    return temp

def solution(p):
    if p == '':
        return ''

    u, v = splitp(p)

    if isright(u):
        return u + solution(v)
    else :
        return '(' + solution(v) + ')' + reversedu(u)

print(solution("(()()))("))