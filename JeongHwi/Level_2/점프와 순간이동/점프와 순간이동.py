def solution(n):
    return str(bin(n))[2:].count("1")
print(solution(5))
print(solution(6))
print(solution(5000))