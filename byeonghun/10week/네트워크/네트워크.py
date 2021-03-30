from collections import deque

def solution(n, computers):
    answer = 0
    net = dict()
    for i in range(n):
        net[i] = 0
    while net:
        first = list(net.keys())[0]
        del net[first]
        que = deque([first])
        while que:
            q = que.popleft()
            for i in range(n):
                if i not in net:
                    continue
                if computers[q][i] == 1:
                    del net[i]
                    que.append(i)
        answer += 1

    return answer

print(solution(3, 
    [[1, 1, 0], 
    [1, 1, 0], 
    [0, 0, 1]]))