from itertools import permutations
import math
## 큰 수 만들기
import time
start = time.time()


def find_prime(number):
    if number <= 1 : return False
    for i in range(2,int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    else : return True


def solution(numbers):
    answer = 0
    nPr = []
    num = set()
    numbers = list(numbers)

    prime = [2]

    count = 0

    for i in range(1,len(numbers)+1):
        nPr.extend(list(permutations(numbers,i)))

    for i in nPr:
        s = ''.join(i)
        num.add(int(s))

    for i in num:
        if find_prime(i):
            count += 1

    return count

print(solution("011"),time.time()-start)



'''
    1.  문제를 보고 
        a. 조합 할 수 있는 숫자를 모두 찾는다.
        b. 숫자들중 소수가 몇개인지 찾는다.
        를 생각하였음
    
    2.  조합 할 수 있는 숫자를 찾기 위해 permutations 함수를 써서 모든 경우의 수에 해당하는 숫자를 찾음

    3.  소수를 판단하는 함수를 따로 만들어 소수를 판단하였다.

    새로 알게 된 점 : permutations 함수.
'''