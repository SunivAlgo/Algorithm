def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[0], reverse= True)
    print(routes)
    while routes:
        car = routes.pop()
        s = car[0]
        e = car[1]
        while routes and e >= routes[-1][0]:
            e = routes[-1][1] if routes[-1][1] < e else e
            routes.pop()
        answer += 1
    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))