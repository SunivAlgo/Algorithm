from collections import deque

def solution(n):
    if n == 1 or n == 2:
        return 1
    box = deque()
    answer = 0
    temp = 0
    for i in range(1, n // 2 + 2):
        box.append(i)
        temp += i
        while True:
            if temp < n:
                break
            elif temp == n:
                answer += 1
                temp -= box.popleft()
            else:
                temp -= box.popleft()
    return answer + 1

print(solution(1000))
