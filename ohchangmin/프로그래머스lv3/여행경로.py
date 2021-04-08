s = ""
answer = []

def dfs(check, tickets, start, cnt, arr):
    if cnt == len(tickets):
        global s
        global answer
        joinArr = "".join(arr)
        if s == "" or s > joinArr:     # 모든 경로 다 지날때 작은 문자열을 답으로 처리하기 위해
            s = joinArr
            answer = arr.copy()
        return

    for i in range(len(tickets)):
        if tickets[i][0] == start and not check[i]:     
            arr.append(tickets[i][0])
            check[i] = True
            if cnt == len(tickets) - 1:     #마지막은 하나 더 추가 해야함
                arr.append(tickets[i][1])
            dfs(check, tickets, tickets[i][1], cnt+1, arr)
            if cnt == len(tickets) - 1:     #마지막은 하나 더 빼야함
                arr.pop()
            check[i] = False
            arr.pop()

def solution(tickets):
    check = [False] * len(tickets)
    dfs(check, tickets, "ICN", 0, [])
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))