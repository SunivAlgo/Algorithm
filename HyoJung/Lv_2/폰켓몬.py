def solution(nums):
    kind=set(nums)
    if len(nums)/2<=len(kind): return len(nums)/2
    else: return len(kind)

    #https://blog.naver.com/leemyo_/222244097375