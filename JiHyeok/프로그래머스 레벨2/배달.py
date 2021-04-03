def solution(N, road, K):
    answer = 0
    
    maps = []
    ###############################################################
    ##맵 초기화 과정 ##
    for i in range(N):
        maps.append([0]*N)
    
    for bridge in road:
        a = bridge[0]
        b = bridge[1]
        weight = bridge[2]

        if maps[a-1][b-1] != 0:
            maps[a-1][b-1] = min(maps[a-1][b-1], weight)
            maps[b-1][a-1] = min(maps[b-1][a-1], weight)
            continue

        maps[a-1][b-1] = weight
        maps[b-1][a-1] = weight

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if maps[i][j] == 0:
                maps[i][j] = 500001 ##무한은 500001로 초기화
    ###############################################################

    ###############################################################

    node = [i for i in range(N)] ## 노드번호를 담은 node 리스트[0,1,2,3,4]
    distance = maps[0] ## 노드 1에서의 모든 노드의 거리를 담은 distance 리스트
    
    while node:

        for_check_min = [distance[i] for i in node] ## 'node 리스트에 있는 노드들의 distance 값' 들을 모은 리스트
        min_node_index = for_check_min.index(min(for_check_min)) ## 위에서 모은 distance 값들 중에, 제일 작은 distance 값을 가진 index 검색
        num_node = node.pop(min_node_index) ## node리스트에서 해당 인덱스 pop
        print(for_check_min)
        print(min_node_index)
        print(num_node)
        '''
        for_check_min ----> [0,1,2,500001,500001,500001]
        min_node_index ------>> 0 = 위의 리스트에서 최소값'0'이 index 0 이므로
        num_node--------> node = [0,1,2,3,4,5] 였는데 pop을 했으니 num_node = 0, node = [1,2,3,4,5] 가 되어있겠지.

        '''
    ###############################################################
    ### 다익스트라 for문 ###
        for i in range(len(distance)):
            distance[i] = min(distance[i], distance[num_node] + maps[i][num_node])
    
    for i in distance:
        if i <= K:
            answer += 1
    ###############################################################
    return answer

## print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))