
def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[1])
    routeidx_for_skip = []

    for i in range(len(routes)):
        if i in routeidx_for_skip: continue
        for j in range(i,len(routes)):
            if routes[j][0] <= routes[i][1]:
                routeidx_for_skip.append(j)
        answer += 1



        
    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))