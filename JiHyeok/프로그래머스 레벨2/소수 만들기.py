from itertools import combinations
import math
def solution(nums):
    answer = 0
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    def prime_number(number):
        for i in range(2,int(math.sqrt(number)) + 1):
            if number % i == 0:
                break
        else :
            return 1
        return 0

    li_nums_combi = list(combinations(nums,3))
    for combi in li_nums_combi:
        
        sum_combi = sum(list(combi))
        answer += prime_number(sum_combi)


    return answer
print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))

'''
    1.  nums에서 3개의 숫자 combination 리스트 만들기
    
    2.  각 combination마다 소수가 되는지 확인하기
'''