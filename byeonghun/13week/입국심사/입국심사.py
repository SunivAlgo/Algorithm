import bisect

def solution(n, times):
    answer = 0
    bisect.bisect(times, 3)
    return times

print(solution(6, [1, 2, 3, 7, 9, 11, 33]))