def solution(s):
    answer = 0
    stack=[]

    for i in s:
        if len(stack)==0: stack.append(i)
        else:
            if stack[-1]==i: stack.pop()
            else: stack.append(i)
    
    if len(stack)!=0: return 0
    return 1

#https://blog.naver.com/leemyo_/222254334393