import re
from collections import deque
def solution(expression):
    priority = [['*', '-', '+'],
                ['*', '+', '-'],
                ['+', '*', '-'],
                ['+', '-', '*'],
                ['-', '*', '+'],
                ['-', '+', '*'],]
    eq = deque(re.findall('\d+|\\*|\\+|\\-', expression))
    values = []
    for i in priority:
        req = eq.copy()
        for j in i:
            leq = deque()
            while req:
                temp = req.popleft()
                if temp == j:
                    leq.append(str(eval(leq.pop() + j + req.popleft())))
                else:
                    leq.append(temp)
            if leq:
                req = leq
        values.append(abs(int(req.pop())))

    return max(values)

print(solution("100-200*300-500+20"))