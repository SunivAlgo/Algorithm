
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
    

    distance = [float('INF')] * n
    distance[0] = 0

    to_visit_node = set([i for i in range(n)])
    node_now = 0

    while len(to_visit_node) != 0:
        to_visit_node.remove(node_now)

        for i in range(len(distance)):
            distance[i] = min(distance[i], distance[node_now] + node_map[node_now][i])
        
        min_value = float('inf')
        min_index = 0
        for i in list(to_visit_node):
            if distance[i] < min_value:
                min_index = i
                min_value = distance[i]

        node_now = min_index
        
    answer = distance.count(max(distance))

    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))