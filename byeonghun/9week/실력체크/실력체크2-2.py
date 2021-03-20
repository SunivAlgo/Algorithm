def solution(brown, yellow):
    answer = []
    a = brown + yellow
    for i in range(1 , a):
        if a % i == 0:
            m = a // i
            if (m - 2) * (i - 2) == yellow:
                return [m , i]
    return answer


print(solution(10,2))