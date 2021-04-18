def solution(tickets):
    answer = []
    edgelist = {}
    for ticket in tickets:
        if ticket[0] not in edgelist:
            edgelist[ticket[0]] = [ticket[1]]
        else:
            edgelist[ticket[0]].append(ticket[1])
        if ticket[1] not in edgelist:
            edgelist[ticket[1]] = []
    for key in edgelist.keys():
        edgelist[key].sort(reverse=True)
    
    que = deque(['ICN'])
    while que:
        now = que.pop()
        answer.append(now)
        while edgelist[now]:
            if edgelist[edgelist[now][-1]] or len(edgelist[now]) == 1:
                que.append(edgelist[now].pop())
                break
            else:
    return answer

print(solution([['ICN','A'],['A','B'],['A','C'],['C','A'],['B','D']]))