from collections import deque

def solution(n, computers):
    answer = 0

    visited=[0]*(n)
    
    for i in range(n):
        q=deque()
        if visited[i]==2: continue
        for j in range(n):
            if visited[j]==2: continue
            if computers[i][j]==1 and visited[j]==0:
                q.append(j)
                visited[j] = 1
        visited[i]=2

        while len(q)!=0:
            s = q.popleft()
            if visited[s]==2: continue

            for k in range(n):
                if computers[s][k]==1 and visited[k]!=2:
                    q.append(k)
                    visited[k]=1
            visited[s]=2
        answer+=1

    return answer


solution(3, 	[[1, 1, 0], [1, 1, 0], [0, 0, 1]])
