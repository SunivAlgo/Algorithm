def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x: x[0])
    check = [False] * len(routes)   
    for i in reversed(range(len(routes))):
        if not check[i]:
            check[i] = True
            answer += 1        
            for j in range(i-1, -1, -1):
                if routes[i][0] <= routes[j][1]:
                    check[j] = True

    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]	))

'''
-20                                                            15
     -18          -13
            -14                   -5
                                  -5            3

이런식으로 먼저 정렬하고 위의 알고리즘을 따라가 본다
'''
#더 빠른 방법
'''
def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    print(routes)
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer
'''