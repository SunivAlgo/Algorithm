def solution(A,B):
    answer = 0
    A.sort(); B.sort(reverse=True)
    for i in range(len(A)): answer+=(A[i]*B[i])
    return answer


#https://blog.naver.com/leemyo_/222244646210
