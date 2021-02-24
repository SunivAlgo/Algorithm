def solution(n):
    ans = 0
    while n > 0:
        r = n % 2
        n = n // 2
        if r == 1:
            ans += 1

    return ans

print(solution(5000))