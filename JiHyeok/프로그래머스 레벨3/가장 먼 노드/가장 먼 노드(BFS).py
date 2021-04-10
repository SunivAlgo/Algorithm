from copy import copy
def solution(n, edge):
    answer = 0
    
    node_map = [[float('INF')] * n for _ in range(n)]

    for bridge in edge:
        node_a_num = bridge[0] - 1
        node_b_num = bridge[1] - 1
        node_map[node_a_num][node_b_num] = 1
        node_map[node_b_num][node_a_num] = 1

    for i in range(len(node_map)):
        node_map[i][i] = 0
    
    print(node_map)
    distance = [float('INF')] * n
    distance[0] = 0
    
    to_visit = [0]
    visited = set()
    count = 1

    while(len(visited) < n):
        temp_set = set()
        for i in to_visit:
            visited.add(i)
            for j in range(len(node_map[i])):
                if j in visited :
                    continue
                if node_map[i][j] == 1:
                    temp_set.add(j)
                    distance[j] = min(distance[j],count)
        print(temp_set)
        count += 1
        to_visit = (list(temp_set))

    answer = distance.count(max(distance))
    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))