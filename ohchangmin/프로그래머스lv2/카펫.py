def solution(brown, yellow):
    answer = []
    size = brown + yellow
    for i in range(3, size):
        x = int(size/i)
        y = int(i)
        if x*y == size and brown == 2*x + 2*y - 4:
            answer.append(x)
            answer.append(y)
            break
        
    return answer

print(solution(24, 24))

'''
카펫의 사이즈를 작은 수 부터 나누는 것을 반복하면서 가로 세로의 경우의 수
들을 찾는다.(정수만 찾는다) 가로 세로의 값으로 갈색값을 구하는 식을 통해 
갈색값과 일치하게 되면 끝난다.  
'''