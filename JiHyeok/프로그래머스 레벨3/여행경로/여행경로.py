import copy
answer = []
def find(tickets, start, path):
    global answer
    for ticket in tickets:
        if ticket[0] == start:
            copy_tickets = copy.deepcopy(tickets)
            copy_path = copy.deepcopy(path)
            destination = ticket[1]
            copy_path += (',' + start)
            copy_tickets.remove(ticket)
            if not copy_tickets: ## 티켓리스트가 없다는 것은 더이상 갈 곳이 없다는 것
                copy_path += ',' + destination
                answer.append(copy_path) ##answer에 path문자열을 저장해둔다.
            find(copy_tickets,destination,copy_path)

def solution(tickets):
    global answer
    for ticket in tickets:
        if ticket[0] == 'ICN': ## 시작이 ICN이어야 하므로 ICN일때 시작
            copy_tickets = copy.deepcopy(tickets)
            destination = ticket[1]
            copy_tickets.remove(ticket)## ICN은 삭제시키고 리스트를 find로 넘겨준다.
            find(copy_tickets,ticket[1],'ICN')## 티켓리스트, 출발지로 해야할 지역, 지금까지 거쳐온 path

    answer = list(min(answer).split(','))
    
    return answer

##print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))