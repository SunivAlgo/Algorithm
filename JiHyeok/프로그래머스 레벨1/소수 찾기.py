import math
def solution(n):
    prime = [2]
    count = 0
    answer = 0
    for i in range (3, n+1):
        for j in prime:
            if i % j == 0:
                count += 1
                break
            if j > math.sqrt(i):
                break
        if count == 0:
            prime.append(i)
        count = 0
    answer = len(prime)
    return answer
'''
    그냥 무턱대고 for문을 두번돌리면서 소수찾기에는 시간이 너무 오래걸림
    따라서
    1. 1 부터 n 까지 prime 리스트(소수 리스트)에 있는 원소들을 나눔.
        나머지가 0 이면 배수라는 것 = 소수가 아니라는 것
        나머지가 있으면 다음 if문을 확인
    2. ex)  n = 47 이면 2,3,5,7 까지만 나눠봐도 소수라는 것을 판별할 수 있음
        따라서 이 수는 소수, prime 리스트에 넣어준다.
'''