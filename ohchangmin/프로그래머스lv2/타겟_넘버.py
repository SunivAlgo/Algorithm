answer = 0

def func(numbers, target, sum, ind):
    if ind == len(numbers):
        if sum == target:
            global answer 
            answer += 1
        return
    
    func(numbers, target, sum + numbers[ind], ind+1)
    func(numbers, target, sum - numbers[ind], ind+1)

def solution(numbers, target):
    func(numbers, target, 0, 0)

    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))

'''
재귀를 사용해서 값을 더하거나 빼서 모든 경우를 살펴봄
전역변수는 global이 필요하다는것을 배움
'''