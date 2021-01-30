from collections import deque
def solution(number, k):
    left = deque()
    right = deque(number)
    while k > 0:
        if not left:
            left.append(right.popleft())
        if not right:
            left.pop()
            k -= 1
            continue
        if left[-1] < right[0]:
            left.pop()
            k -= 1
        else :
            left.append(right.popleft())
    if right:
        left.extend(right)
    return ''.join(left)

print(solution("4177252841", 4))