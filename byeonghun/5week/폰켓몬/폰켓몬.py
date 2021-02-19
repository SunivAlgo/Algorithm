def solution(nums):
    pocketmondict = {}
    for i in nums:
        if i not in pocketmondict:
            pocketmondict[i] = 1
        else:
            pocketmondict[i] += 1
    
    variable = len(pocketmondict.keys())
    if variable > (len(nums) // 2):
        return len(nums) // 2
    else:
        return variable

print(solution([3,3,3,2,2,2]))