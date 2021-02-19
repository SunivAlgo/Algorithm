def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)

    for i in range(0, len(A)):
        answer += A[i]*B[i]

    return answer

A = [1, 4, 2]
B = [5, 4, 4]
print(solution(A,B))

'''
for i, j in zip(A, B):
알아둘 것
'''