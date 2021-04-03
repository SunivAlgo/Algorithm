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
'''