from itertools import permutations
from copy import deepcopy

def opOrder(exp):
    op_list=list()
    if '+' in exp: op_list.append('+')
    if '*' in exp: op_list.append('*')
    for i in range(len(exp)):
        if exp[i]=='-' and i!=0:
            if exp[i-1].isnumeric():
                op_list.append('-'); break
    return list(permutations(op_list,len(op_list)))

def str_split(exp):
    tmp=""
    exp_list=[]
    for i in range(len(exp)):
        if exp[i].isnumeric(): tmp+=exp[i]
        else:
            exp_list.append(int(tmp))
            exp_list.append(exp[i])
            tmp=""
    exp_list.append(int(tmp))
    return exp_list

def calc(a,op,b):
    if op=='+': return a+b
    elif op=='-': return a-b
    else: return a*b

def solution(expression):
    answer = 0
    op_order=opOrder(expression)
    exp_list =str_split(expression)

    for i in range(len(op_order)):
        tmp_list=deepcopy(exp_list)
        for j in range(len(op_order[i])):
            while op_order[i][j] in tmp_list:
                idx=tmp_list.index(op_order[i][j])
                tmp=calc(tmp_list[idx-1],tmp_list[idx],tmp_list[idx+1])
                tmp_list[idx-1]=tmp
                tmp_list.pop(idx)
                tmp_list.pop(idx)
        answer=max(answer,abs(tmp_list[0]))    
    return answer

#https://blog.naver.com/leemyo_/222249815190