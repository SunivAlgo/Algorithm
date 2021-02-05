from collections import deque
def solution(number, k):
    right = deque(map(int,list(number)))
    left = []

    while right:
        while left and right[0] > left[-1] :
            left.pop()
            k -= 1
            if k <= 0:
                left = left + list(right)
                left = ''.join(list(map(str,left)))
                return left
        left.append(right.popleft())
    left = ''.join(list(map(str,left[0 : len(left) - k])))
    return left

print(solution("9"*1000000,999999))