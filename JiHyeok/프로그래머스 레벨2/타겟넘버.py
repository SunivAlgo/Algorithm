
def play(numbers, target, index):
    if index == len(numbers):
        if sum(numbers) == target:
            return 1
        else : return 0
    else :
        a = play(numbers,target,index + 1)
        numbers[index] *= (-1)
        b = play(numbers,target,index + 1)
    return a + b

            
def solution(numbers, target):
    
    answer = play(numbers,target,0)

    return answer
print(solution([1,1,1,1,1],3))
'''
    인터넷에서 참고하여 코딩하였음.
    
    1.  결국에는 모든 경우의 수를 따져서 타겟넘버가 되었는지 안되었는지 알아내야 함.
    2.  알아내는것에 재귀 함수 사용
        
'''