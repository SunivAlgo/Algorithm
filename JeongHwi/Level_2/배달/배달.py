from collections import deque
from pprint import pprint

def search(graph,weight,K):
    q = deque([])
    q.append(graph[1])
    while q:
        next_node = q.popleft()
        for start,dest,wei in next_node:
            if weight[dest] > weight[start]+wei:
                weight[dest] = weight[start]+wei
                q.append(graph[dest])
            else:
                continue
    return len([x for x in weight[1:] if x<=K])


def solution(N,road,K):
    graph = {}
    
    # initialize Graph
    for s,d,w in road:
        if s not in graph:
            graph[s] = [(s,d,w)]
        else:
            graph[s].append((s,d,w))
        
        if d not in graph:
            graph[d] = [(d,s,w)]
        else:
            graph[d].append((d,s,w))
    
    pprint(graph)

    glen = len(graph)
    weight = [float("inf") if i>1 else 0 for i in range(glen+1)]
    
    return search(graph,weight,K)


print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))
print(solution(6,[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]],4))