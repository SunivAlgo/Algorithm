from collections import deque
def solution(number, k):
    start_Index = 0
    End_Index = k + 1
    answer = list(map(int,list(number))) 
    
    while k > 0:
        if k >= len(answer[start_Index:]):
            while k > 0:
                answer.pop(start_Index)
                k -= 1
        else :
            if answer[start_Index] == 9:
                start_Index += 1
                End_Index = start_Index + k + 1
            else :
                comparison = answer[start_Index : End_Index]
                max_number = max(comparison)
                while answer[start_Index] != max_number:
                    answer.pop(start_Index)
                    k -= 1
                start_Index += 1
                End_Index = start_Index + k + 1
        
    answer = ''.join(map(str,answer))


    return answer
print(solution("978444444",4))

'''
    1.  k == length 이면 모두 팝해버리면 됨.
    2.  k != length 이면 max값을 찾을 때 까지 pop하면 됨.
'''
