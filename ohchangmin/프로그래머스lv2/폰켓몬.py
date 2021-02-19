def solution(nums):
    d = {}

    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    if len(nums)/2 < len(d):
        return len(nums)/2

    return len(d)

nums = [3,3,3,2,2,4]
print(solution(nums))

'''
딕셔너리에 nums의 값들을 넣는다.
딕셔너리 길이와 nums/2의 길이를 비교해 반환한다.
'''