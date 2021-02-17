from itertools import permutations
mx = 0
def cal(a,b,operator):
    if operator == '+':
        return a+b
    if operator == '-':
        return a-b
    if operator == '*':
        return a*b

def calculation(expression,operator):
    li_expression = []
    s = ''
    global mx
    ### 문자열 파싱 '50*6-3*2' -> [50,'*',6,'-',3,'*',2] 식으로
    for i in range(len(expression)): 
        if expression[i] in operator:
            li_expression.append(int(s))
            li_expression.append(expression[i])
            s = ''
        else :
            s += expression[i]
    li_expression.append(int(s))
    ###  [50,'*',6,'-',3,'*',2] 에서 * 가 1순위 이면 [300,'-',3,'*',2] 이런식으로 바꾸는 과정
    for op in operator:
        while op in li_expression:
            i = li_expression.index(op)
            n = cal(li_expression[i-1],li_expression[i+1],li_expression[i])
            li_expression[i] = n
            li_expression.pop(i+1)
            li_expression.pop(i-1)
    
    if abs(li_expression[0]) > mx:
        mx = abs(li_expression[0])



def solution(expression):
    operators = ['+','-','*']
    ### 연산자의 우선순위 정하기
    li_operators = list(permutations(operators,3))
    ### 우선순위가 정해진 연산자 리스트들(6개)을 calculation 함수로 넘김
    for operator in li_operators:
        calculation(expression,operator)
    answer = mx
    return answer


print(solution("50*6-3*2"))

