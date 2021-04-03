from itertools import permutations,combinations
def solution(nums):
    new_nums = list(set(nums))
    len_nums = len(nums)
    len_new_nums = len(new_nums)
    
    if len_new_nums > len_nums//2:
        answer = len_nums//2
    else:
        answer = len_new_nums
    return answer
 
print(solution([3,3,3,2,2,2]))


   '''
    1.  nums를 집합에 넣어주어 중복되는 숫자들을 제거 한다.
    2.  new_nums 가 nums의 길이 / 2 보다 크다면 nums의 길이/2 return
    3.  그게 아니라면 new_nums 의 길이 return
    '''