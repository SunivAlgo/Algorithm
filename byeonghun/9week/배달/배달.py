from collections import deque

def solution(N, road, K):
    edgelist = dict()
    for i in range(N):
        edgelist[i + 1] = []
    for i in range(len(road)):
        edgelist[road[i][1]].append((road[i][0], road[i][2]))
        edgelist[road[i][0]].append((road[i][1], road[i][2]))
    
    print(edgelist)
    dist = { i:float('inf') if i != 1 else 0 for i in range(1, N+1) }
    que = deque([1])
    while que:
        cur_node = que.popleft()
        for nxt_node, d in edgelist[cur_node]:
            if dist[nxt_node] > dist[cur_node] + d:
                dist[nxt_node] = dist[cur_node] + d
                que.append(nxt_node)

    return len([True for dist in dist.values() if dist <= K])

print(solution(	5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))