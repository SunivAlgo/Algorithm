
def solution(n, edge):
    distance = [float('inf')] * n
    distance[0] = 0
    answer = 0
    visited_node = set()
    node_dic = dict()
    start_node = 1
    for e in edge:
        if e[0] not in node_dic:
            node_dic[e[0]] = [e[1]]
        else:
            node_dic[e[0]].append(e[1])

        if e[1] not in node_dic:
            node_dic[e[1]] = [e[0]]
        else:
            node_dic[e[1]].append(e[0])

    while(visited_node < n):
        for i in node_dic[start_node]:
            

    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))