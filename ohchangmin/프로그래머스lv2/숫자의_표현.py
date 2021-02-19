def solution(n):
    answer = 0
    for i in range(1, n+1):
        s = 0
        for j in range(i, n+1):
            s += j
            if s == n:
                answer+=1
            elif s > n:
                break

    return answer

print(solution(15))

'''
2중 for문 사용
'''