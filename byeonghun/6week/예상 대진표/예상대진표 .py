import math
def solution(n,a,b):
    answer = 1
    while math.ceil(a/2) != math.ceil(b/2):
        a = math.ceil(a/2)
        b = math.ceil(b/2)
        answer += 1
    return answer

print(solution(8, 2, 3))