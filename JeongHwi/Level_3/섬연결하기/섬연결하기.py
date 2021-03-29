from collections import deque
# 다익스트라로 풀려다 실패함 --> 크루스칼
parent = {}
rank = {}
def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v,node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    # union - by - rank
    if rank[root1] > rank[root2]: # root1의 랭크가 root2보다 높다면 root2는 root1의 자식이됨
        parent[root2] = root1
    else:
        parent[root1] = root2 # 반대면 root1이 root2의 자식이됨
        if rank[root1] == rank[root2]: # 같으면 root2의 랭크 ++
            rank[root2] += 1

def solution(n,costs):
    mst = 0
    
    for i in range(n):
        parent[i] = i
        rank[i] = 0

    costs.sort(key=lambda x:x[2])
    for v,u,c in costs:
        if find(v) != find(u): # Cycle Check
            union(v,u)
            mst+=c
    return mst

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))
print(solution(4,[[0,1,1],[0,2,2],[2,3,1]]))
print(solution(4,[[0, 1, 5], [1, 2, 3], [2, 3, 3], [3, 1, 2], [3, 0, 4]]))