def solution(s):
    stack = []
    answer = 1
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    if stack:
        answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer
print(solution('baabaa'))
print(solution('cdcd'))
'''
    stack이 없으면 -> push
    
    있으면 -> stack[-1] 이 지금 push하려는 원소와 같으면 pop,  다르면 push
'''