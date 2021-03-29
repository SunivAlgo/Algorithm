# Kruskal's Algorithm

* MST (Minimum Spanning Tree) , 최소 신장 트리
* 싸이클 X 

* Union-Find 알고리즘을 기반으로 함
  * Disjoint Set을 표현할 때 사용



#### Union - Find

* 두 개별 집합을 하나의 집합으로 합침 --> 두 트리를 하나의 트리로 만듬 (Union)
* 여러 노드가 존재할 때, 두 개의 노드를 선택해서, 현재 두 노드가 서로 같은 그래프에 속하는지 판별하기 위해, 각 그룹의 최상단 원소 (루트노드를 확인)



#### Kruskal

* 간선을 거리가 짧은 순서대로 그래프에 포함
  * 모든 노드들을 최대한 적은 비용으로 "연결"만 시킴
* 싸이클이 만들어지면 안됨, 노드가 같은 최상위 정점을 갖는지 확인

> 1. 정렬된 순서에 맞게 노드를 그래프에 포함
> 2. 포함시키기 전에는 사이클 테이블 확인
> 3. 사이클을 형성하는 경우 간선포함 X



#### 예시문제 : 섬 연결하기

```python
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
```





#### Reference

[잔재미코딩](https://www.fun-coding.org/Chapter20-kruskal-live.html)