
def solution(n, costs):
    answer = 0
    costmap = []
    '''
    배열 모두 0으로 초기화 ex) n = 4
    0 0 0 0 
    0 0 0 0 
    0 0 0 0 
    0 0 0 0 
    '''
    for _ in range(n):
        costmap.append([0]*n)
    
    '''
    costs의 value 값을 모두 넣어줌
    0 1 2 0
    1 0 5 1 
    2 5 0 8
    0 1 8 0
    '''
    
    

    for cost in costs:
        a, b, value = cost[0], cost[1], cost[2]
        costmap[a][b], costmap[b][a] = value, value
    

    print(costmap)
    connected_island_list = [] ## 현재 연결된 섬들을 나타내는 리스트

    while(len(connected_island_list) < n): ## connected_island_list == n 일시 모든 섬이 연결된 것이므로 끝
        
        if not connected_island_list : ## 처음에 연결된 섬이 아무것도 없을시, 그냥 0번 섬을 넣고, continue
            connected_island_list.append(0)
            continue
        
        min_cost = float('inf') ## 현재 연결된 섬들 중에서 제일 낮은 cost로 연결된 섬을 판별하기 위한 min_cost
        min_cost_island_id = None ## min_cost로 선정된 섬의 id
        
        for island_id in connected_island_list: ## 현재 연결된 섬들중에서 제일 낮은 cost를 찾아야 하므로 connected_island_list를  하나씩 순회
            for i in range(len(costmap[island_id])): 
                if costmap[island_id][i] != 0 and costmap[island_id][i] < min_cost: ## 현재 연결된 섬들중 고른 island _id와 연결된(= cost가 0이 아닌) 섬들 중에서 min_cost를 추출
                    min_cost = costmap[island_id][i]
                    min_cost_island_id = i
        ## min_cost, min_cost_island_id 추출 완료
        connected_island_list.append(min_cost_island_id) ## 현재 연결된 섬 리스트에 이어 붙인다
        answer += min_cost ## answer에 min_cost 플러스

        for island_id in connected_island_list: ## 이제 연결되었기 때문에, 기존에 연결된 섬들끼리의 cost는 0으로 만드는 작업
            costmap[min_cost_island_id][island_id],costmap[island_id][min_cost_island_id] = 0,0

    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))