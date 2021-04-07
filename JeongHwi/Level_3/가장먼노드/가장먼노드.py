from collections import deque

def bfs(graph,visit,start):
    
    q = deque()
    q.append(start)
    visit[start] = 1
    max_node = 1
    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if visit[next_node] == 0:
                visit[next_node] = visit[now]+1
                max_node = max(max_node,visit[next_node])
                q.append(next_node)
            else:
                continue
    return visit.count(max_node)
    
def solution(n,edge):
    # init
    graph = {}
    for a,b in edge:
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        
        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)
    
    visit = [0 for _ in range(n+1)]
    return bfs(graph,visit,1)


print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]),3)
