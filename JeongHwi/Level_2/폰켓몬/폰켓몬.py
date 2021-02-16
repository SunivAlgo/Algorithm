def solution(nums):
    n = len(nums)//2
    count = 0
    ans = set()
    for x in nums:
        if x in ans:
            continue
        ans.add(x)
        count += 1
        if n == count:
            break
    return len(ans)


print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))