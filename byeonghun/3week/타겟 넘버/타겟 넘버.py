
def recursive(numbers, i, value, target):
    if i == len(numbers):
        if value == target:
            return 1
        else:
            return 0
    return recursive(numbers, i+1, value + numbers[i], target) + recursive(numbers, i+1, value - numbers[i], target)

def solution(numbers, target):
    return recursive(numbers, 0, 0, target)

print(solution([1,1,1,1,1], 3))