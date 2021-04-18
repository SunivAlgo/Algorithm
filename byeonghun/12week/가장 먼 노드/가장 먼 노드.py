from collections import deque

def solution(n, edge):
    distance = 1
    edgelist = {i : [] for i in range(1, n + 1)}
    visited = {i : 0 for i in range(1, n + 1)}
    for i in edge:
        edgelist[i[0]].append(i[1])
        edgelist[i[1]].append(i[0])
    que = deque([1])
    visited[1] = -1
    answer = 0
    while que:
        que2 = deque()
        while que:
            now = que.popleft()
            for e in edgelist[now]:
                if visited[e] == 0:
                    que2.append(e)
                    visited[e] = distance
        que = que2
        if que:
            answer = len(que)
        distance += 1
    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))