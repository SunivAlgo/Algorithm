

def solution(prices):
    answer = []
    for i in range(0, len(prices)):
        c = 0
        for j in range(i+1, len(prices)):
            c+=1
            if prices[j] < prices[i]:
                break
        answer.append(c)
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))

"""
단순히 리스트의 값을 모두 참조하여 값 뒤에 더 작은 값이
나올 때 까지 카운트를 1씩 증가시켜서 그 값을 답에 넣었다.
"""
    
