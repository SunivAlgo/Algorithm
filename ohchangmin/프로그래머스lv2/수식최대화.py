from itertools import permutations

def solution(expression):
    answer = 0
    operator = []
    if '*' in expression:
        operator.append('*')
    if '-' in expression:
        operator.append('-')
    if '+' in expression:
        operator.append('+')
    p_operator = list(permutations(operator))

    n = ""
    s = []
    for i in expression:
        if i >= "0" and i <= "9":
            n += i
        else:       
            s.append(int(n))
            s.append(i)
            n = ""
    s.append(int(n))
  
    for i in p_operator:
        s_temp = s
        for j in i:
            k = 0
            temp = []
            while k < len(s_temp):
                if s_temp[k] == j:
                    if s_temp[k] == '*':
                        temp[-1] *= s_temp[k+1]
                    if s_temp[k] == '+':
                        temp[-1] += s_temp[k+1]
                    if s_temp[k] == '-':
                        temp[-1] -= s_temp[k+1]
                    k += 2
                else:
                    temp.append(s_temp[k])
                    k += 1
            s_temp = temp
        if answer < abs(s_temp[0]):
            answer = abs(s_temp[0])
                
    return answer

expression = "100-200*300-500+20"
print(solution(expression))

'''
먼저 expression에 어떤 연산자가 있는지 확인 후 존재하는 연산자의 
모든 순열을 구한다. expression 문자열을 [100, '-', 200, '*', 300, '-', 500, '+', 20] 
이러한 방식으로 리스트에 저장한다. 연산자의 모든 순열의 경우의 수대로 연산을 차례대로 진행 한다.
'''
