def solution(n, costs):
    answer = 0
    vertices = {0:0}
    edgelist = {}
    for i in range(1,n):
        vertices[i] = float('inf')

    for cost in costs:
        if cost[0] not in edgelist:
            edgelist[cost[0]] = [[cost[1], cost[2]]]
        else:
            edgelist[cost[0]].append([cost[1], cost[2]])
        if cost[1] not in edgelist:
            edgelist[cost[1]] = [[cost[0], cost[2]]]
        else:
            edgelist[cost[1]].append([cost[0], cost[2]])

    while vertices:
        min_key = min(vertices.keys(), key=lambda k: vertices[k])
        vertex = [min_key, vertices[min_key]]
        del vertices[min_key]
        answer += vertex[1]
        for edge in edgelist[vertex[0]]:
            if edge[0] in vertices and vertices[edge[0]] > edge[1]:
                vertices[edge[0]] = edge[1]
    return answer

print(solution(	4, 
    [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))