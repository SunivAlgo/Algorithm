def solution(n):
    n_1 = 1
    n_2 = 0
    answer = 1
    for _ in range(n - 1):
        answer = n_1 + n_2
        n_2 = n_1
        n_1 = answer
    return answer % 1234567

print(solution(10))