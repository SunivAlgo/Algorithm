"""
+ - * 만으로 연산 수식 전달
우선순위 자유롭게 재정의 -> 큰 숫자 제출
같은 순위 연산자 X , +,* > -  (X)  2개의 연산자가 동일한 순위를 가지도록 정의 X
값이 음수면 절댓값
"""
# from itertools import permutations
# def solution(expression):
#     max_ = -1
#     for x in permutations(["+","-","*"]):
#         split3 = ["("+s+")" for s in expression.split(x[2])]
#         split2 = ["("+x[1].join(s)+")" for s in list(map(lambda s:s.split(x[1]),split3))]
#         split1 = ["("+x[0].join(s)+")" for s in list(map(lambda s:s.split(x[0]),split2))]
#         max_ = max(max_,abs(eval(x[2].join(split1))))
#     return max_
#     #왜 틀린지 모르겠음
from itertools import permutations
import re
def solution(expression):
    max_ = -1
    for x in permutations(["+","-","*"]):
        numbers = re.findall("\d+",expression)
        nlen = len(numbers)
        operation = re.findall("\W",expression)
        exp = expression
        st = [int(numbers[0])]
        opst = []
        for op in x:
            for i in range(1,nlen):
                if op != operation[i-1]:
                    opst.append(operation[i-1])
                    st.append(int(numbers[i]))
                else:
                    new_value = eval(str(st.pop())+op+str(numbers[i]))
                    st.append(new_value)
            operation=opst
            numbers=st
            st=[numbers[0]]
            opst=[]
            nlen = len(numbers)
        max_ = max(max_,abs(numbers[0]))
    return max_
                
                


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
print(solution("2-990-5+2"))
print(solution("2-990-5+2+3*2"))

# ('+', '-', '*')
# ['100', '200', '300', '500', '20'] ['-', '*', '-', '+']