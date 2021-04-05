def solution(n, costs):
    costs = sorted(costs, key=lambda x : x[2]) #가장 작은 다리부터 추가해야 함
    island = [i for i in range(n)] # 섬들의 집합을 나타내는 리스트
    answer = 0
    cnt = 0
    for cost in costs:
        if island[cost[0]] != island[cost[1]]: #삼각형이 나오지 않게함
            answer += cost[2]
            cnt += 1
            p1 = island[cost[0]] # 이 부분을 설정하지 않고 바로 island[cost[0]], island[cost[1]] 을 사용하여 많이 해맴
            p2 = island[cost[1]]
        for i in range(len(island)): #조직을 통일함
            if island[i] == p1:
                island[i] = p2

        if cnt == n-1: #다리의 수가 n-1 개면 끝
            break   
    return answer

#print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
#print(solution(5, [[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]]))
print(solution(5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]]))
#print(solution(2, [[0,1,10]]))

'''
크루스칼 알고리즘 사용
내가 짠 코드는 효율이 밑에 코드보다 효율이 안 좋음
'''

'''
def solution(n, costs):
    # kruskal algorithm
    ans = 0
    costs.sort(key = lambda x: x[2]) # cost 기준으로 오름차순 정렬
    routes = set([costs[0][0]]) # 집합

    while len(routes)!=n:
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                ans += cost[2]
                costs[i] = [-1, -1, -1]
                break

    return ans
'''    