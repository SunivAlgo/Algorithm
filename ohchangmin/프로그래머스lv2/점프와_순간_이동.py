def solution(n):
    ans = 0
    
    while n != 0:
        if n % 2 == 1:
            n -= 1
            ans += 1
        n //= 2

    return ans

print(solution(5000))

'''
n 이 0일때 까지 반복
홀수면 -1을 하고 결과값에 1을 추가
n은 2로 계속나눈다.

n을 이진법으로 표현 후 1의 갯수를 세어도 답이 나옴
'''