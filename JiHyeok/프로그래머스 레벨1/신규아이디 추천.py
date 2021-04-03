import copy
    
def solution(new_id):
    switch = 0
    answer = ''
    permit = ['a','b','c','d','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    permit += ['1','2','3','4','5','6','7','8','9','0']
    permit += ['-','_','.']

    new_id = new_id.lower() ### 1단계

    for s in new_id:    ### 2단계
        if s in permit:
            answer += s
    
    new_id = copy.deepcopy(answer)
    answer = ' '

    for s in new_id:    ### 3단계
        if s == '.':
            if answer[-1] == '.':
                continue
        answer += s
    answer = answer[1:]
    
    if answer:
        if answer[0] == '.': ### 4단계
            answer = answer[1:]
    if answer:
        if answer[-1] == '.':
            answer = answer[:-1]

    if not answer:  ### 5단계
        answer += 'a'

    if len(answer) >= 16: ### 6단계
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer [:14]

    if len(answer) <= 2: ### 7단계
        while len(answer) < 3:
            answer += answer[-1]


    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("abcdefghijklmn.p"))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
print(solution('a.b.c.d.'))

'''
그저 단계별 설명대로 코딩하였음

'''