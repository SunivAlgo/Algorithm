def solution(n,a,b):
    answer = 0
    if a > b:
        a,b = b,a

    while a != b:
        if a % 2 == 1:
            a += 1
        if b % 2 == 1:
            b += 1
        a /= 2
        b /= 2
        answer += 1
    return answer

print(solution(32,8,18))
'''
    1.  대진이 붙으려면 바로 홀수, 짝수 순의 바로 옆숫자여야 할 수 밖에 없다.

    2.  결국 같은 숫자가 될 때까지 2로 나눠주면 됨

    3.  ex) 8 18 -> 4 9 -> 2 5 -> 1 3 -> 1 2 총 5 번
'''
