# 가장 먼 노드

###### 문제 설명

n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

##### 제한사항

- 노드의 개수 n은 2 이상 20,000 이하입니다.
- 간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
- vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.

##### 입출력 예

| n    | vertex                                                   | return |
| ---- | -------------------------------------------------------- | ------ |
| 6    | [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]] | 3      |

##### 입출력 예 설명

예제의 그래프를 표현하면 아래 그림과 같고, 1번 노드에서 가장 멀리 떨어진 노드는 4,5,6번 노드입니다.

![image.png](./figure/README/dec85ab5-0273-47b3-ba73-fc0b5f6be28a.png)

### Code

```python
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

```

### Solution

단순한 Graph 문제, 최대 높이를 탐색하면 됨

나는 BFS로 최대 높이를 탐색하였고 `max_node` 라는 변수를 두어 가장 깊은 노드의 높이를 저장하였다.

Max 함수 대신 그냥 if 문으로 처리하면 더 빠를 것 같음!

`+3`