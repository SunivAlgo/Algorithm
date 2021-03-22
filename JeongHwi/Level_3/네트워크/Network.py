from collections import deque
def solution(n, computers):
    visit=[0 for _ in range(n)]
    count=0
    q=deque()
    for i in range(n):
        if not visit[i]:
            count+=1
            visit[i] = 1
            q.append(i)
            while q:
                nownode=q.popleft()
                for j in range(n):
                    if i!=j and not visit[j] and computers[nownode][j]:
                        q.append(j)
                        visit[j] =1
    return count