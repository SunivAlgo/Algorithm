def solution(prices):
    answer = []
    stack = []
    count = 0
    for i in range (0,len(prices)):
        answer.append(-1)
    
    stack.append(0)
    for i in range(1,len(prices)):
        if stack : ## 스택이 비어있지 않으면
            if prices[i] < prices[stack[-1]]:
                while prices[i] < prices[stack[-1]]:
                    
                    answer[stack[-1]] = i - stack[-1]
                    stack.pop()
                    if not stack :
                        break
            stack.append(i)

        else :  ## 스택이 비어있으면
            stack.append(i)
    
    for i in stack:
        answer[i] = len(prices) - i -1
    
    return answer
print(solution([1, 2, 3, 2, 3]))

'''
    풀이봤음.
    1. stack에 index를 저장하는 방식으로 풀었음.
'''