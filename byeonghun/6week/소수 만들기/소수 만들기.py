from itertools import combinations
import math
def eratos(n):
    e = [True for _ in range(n+2)]
    e[1] = False
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        j = i + i
        while j <= n:
            e[j] = False
            j += i
    return e

        
def solution(nums):
    answer = 0
    limit = 0
    nums.sort(reverse=True)
    for i in range(3):
        limit += nums[i]
    e = eratos(limit)
    
    combinum = list(combinations(nums, 3))
    for i in combinum:
        if e[sum(i)]:
            answer += 1
    return answer
print(solution([1,2,7,6,4]))