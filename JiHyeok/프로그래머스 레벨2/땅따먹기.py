

def solution(land):
    answer = 0
    print('Hello Python')
    idx = 5
    for i in range(1,len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    
    return max(land[-1])
print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))
'''

    1.  for문을 돌릴 때  전행의 j열을 제외한 배열의 max값을 지금행의 열의 값에 더해주며 내려간다.
    
    
    ***풀이 참고하였음***
'''