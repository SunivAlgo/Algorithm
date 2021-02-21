def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    sums = 0
    for i in zip(A,B):
        sums = sums+(i[0]*i[1])
    return sums

print(solution([1,4,2],[5,4,4]))