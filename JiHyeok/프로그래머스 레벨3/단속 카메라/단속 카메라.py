'''
추석트래픽과 비슷하게 생각했음
1. 구간이 끝나는 순으로 routes 정렬
2. routes[i][1] > routes[j][0] 이면 j를 모두 skip list에 넣었음
3. skip list에 있으면 계산 skip
'''
def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[1]) ## 구간의 끝 순서로 routes 정렬
    routeidx_for_skip = [] ## skip해도 되는 route를 넣어놓은 리스트

    for i in range(len(routes)): ## routes 순회
        if i in routeidx_for_skip: continue ## skip 리스트에 있으면 continue
        for j in range(i,len(routes)): ## i부터 routes의 끝까지 순회
            if routes[j][0] <= routes[i][1]: ## 시작점이 routes[i][1] 보다 작으면 skip에 넣음
                routeidx_for_skip.append(j)
        answer += 1 ## answer 증가
    


        
    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))