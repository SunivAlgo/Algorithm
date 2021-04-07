# [start, dest]
from pprint import pprint

from sys import setrecursionlimit
setrecursionlimit(10**8)
import copy 

answer = []
def back(now,ticket,count_Tic,ticket_len,count,route):
    global answer
    if ticket_len == count:
        way = copy.deepcopy(route)
        answer.append(way)
        return True
    if now in ticket:
        for next_airport in ticket[now]:
            if count_Tic[next_airport] == 0: # 더 이상 다음 공항에 도착할 티켓이 없는 경우
                continue
            # 이 밑으로는 다음 공항에 도착할 티켓이 있는 경우
                
            route.append(next_airport)
            count_Tic[next_airport]-=1
            back(next_airport,ticket,count_Tic,ticket_len,count+1,route)
            route.pop()
            count_Tic[next_airport]+=1
    

def solution(tickets):
    ticket = {}
    count_Tic = {}
    visit = {}
    
    # init 
    for start,dest in tickets:
        if start not in ticket:
            ticket[start] = [dest]
        else:
            ticket[start].append(dest)
            ticket[start].sort()
        # 해당 도시에 도착하는 티켓의 개수
        if dest not in count_Tic:
            count_Tic[dest] = 1
        else:
            count_Tic[dest] += 1
    ticket_len = len(tickets)+1
    back("ICN",ticket,count_Tic,ticket_len,1,["ICN"])
    return answer[0]
    

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]),["ICN", "JFK", "HND", "IAD"])
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]),["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
# print(solution([['ICN','AAA'],['ICN','AAA'],['ICN','AAA'],['AAA','ICN'],['AAA','ICN']]))
# print(solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]))

# print(solution([["ICN", "JFK"], ['HND', 'IAD'], ['JFK', 'HND']]), "\n",['ICN', 'JFK', 'HND', 'IAD'])
# answer= []
# print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], [ 'ATL', 'SFO']]), "\n",['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO'])
# answer= []
# print(solution([['ICN', 'B'], ['B', 'ICN'], ['ICN', 'A'], [ 'A', 'D'], ['D', 'A']]), "\n",['ICN', 'B', 'ICN', 'A', 'D', 'A'])
# answer= []
# print(solution([['ICN', 'SFO'], ['SFO', 'ICN'], ['ICN', 'SFO'],['SFO', 'JFK']]), "\n",['ICN', 'SFO', 'ICN', 'SFO', 'JFK'])
# answer= []
# print(solution([['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN'],['A', 'C']]), "\n",['ICN', 'A', 'ICN', 'A', 'C'])
# answer= []
# print(solution([['ICN', 'A'], ['A', 'ICN'], ['A', 'B'],['ICN', 'A']]), "\n",['ICN', 'A', 'ICN', 'A', 'B'])
# answer= []
# print(solution([['ICN', 'BBB'], ['AAA', 'ICN'], ['ICN', 'AAA']]),"\n",['ICN', 'AAA', 'ICN', 'BBB'])
# answer= []
# print(solution([['ICN', 'ABB'], ['AAA', 'ICN'], ['ICN', 'AAA'], ['ICN', 'ADD'], [ 'ABB', 'ICN']]), "\n",['ICN', 'AAA', 'ICN', 'ABB', 'ICN', 'ADD'])
# answer= []
# print(solution([['ICN', 'AAA'], ['ICN', 'AAA'], ['AAA', 'ICN'],['AAA', 'CCC']]), "\n",['ICN', 'AAA', 'ICN', 'AAA', 'CCC'])
# answer= []
print(solution([['ICN', 'AAA'], ['ICN', 'AAA'], ['ICN', 'AAA'],['AAA', 'ICN'], ['AAA', 'ICN']]), "\n", ['ICN', 'AAA', 'ICN', 'AAA', 'ICN', 'AAA'])
answer= []
# print(solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]),"\n",["ICN", "B", "ICN", "A"])

# print(solution([['ICN','A'],['A','B'],['A','C'],['C','A'],['B','D']]))
print(solution([["ICN","A"],["ICN","A"],["A","B"]]))