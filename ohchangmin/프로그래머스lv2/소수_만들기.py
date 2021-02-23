from itertools import combinations

def solution(nums):
    answer = 0

    c = list(combinations(nums, 3))
    for i in c:
        n = sum(i)
        flag = True
        for j in range(2, int(n**0.5) + 1):
            if n % j == 0:
                flag = False
                break
        if flag:
            answer += 1

    return answer

nums = [1,2,3,4]
print(solution(nums))

'''
인자 배열의 조합을 구한후 각각의 경우의 조합의 합을 for문을 통해
소수판별을 한다.
(for문이 끝나고 flag를 사용하지 않고 else를 써도 되는것을 알았다.)
'''