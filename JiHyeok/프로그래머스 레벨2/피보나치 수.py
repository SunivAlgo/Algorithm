
def solution(n):
    li = [0,1]
    answer = 0
    for i in range (2,n+1):
        number = li[i - 2] + li[i - 1]
        li.append(number)


    return li[-1] % 1234567

print(solution(5))
'''
    1.  1 <= n <= 100000 이므로 재귀를 쓰기에는 함수호출이 너무 많이 됨

    2.  리스트에 저장하면서 i 번째 피보나치 수는 i-1, i-2의 index를 참조하도록 코드 구현
'''