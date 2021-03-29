# 섬 연결하기

###### 문제 설명

n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.

다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

**제한사항**

- 섬의 개수 n은 1 이상 100 이하입니다.
- costs의 길이는 `((n-1) * n) / 2`이하입니다.
- 임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
- 같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
- 모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
- 연결할 수 없는 섬은 주어지지 않습니다.

**입출력 예**

| n    | costs                                     | return |
| ---- | ----------------------------------------- | ------ |
| 4    | [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]] | 4      |

**입출력 예 설명**

costs를 그림으로 표현하면 다음과 같으며, 이때 초록색 경로로 연결하는 것이 가장 적은 비용으로 모두를 통행할 수 있도록 만드는 방법입니다.

![image.png](figure/README/f2746a8c-527c-4451-9a73-42129911fe17.png)

### Code

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

### Solution

처음 시도는 다익스트라로 시도하였다.

하지만 다익스트라와 크루스칼의 차이점은 정점이 다 이어지느냐 안이어지느냐 이다.

**크루스칼**은 MST를 구할 때 대표적인 알고리즘

해당 문제는 MST를 구하는 것이기 때문에 크루스칼 문제에 해당 (Prim으로도 가능)

크루스칼에 대한 설명은 다음과 같음

[크루스칼 설명](../../Docs/Kruskal.md)

 `+4`