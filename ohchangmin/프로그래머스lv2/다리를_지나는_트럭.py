from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque(truck_weights)
    bridge = deque()
    for i in range(0, bridge_length):
        bridge.append(0)

    sum = 0
    while True:
        sum -= bridge.popleft()
        if q and weight - sum >= q[0]:
            n = q.popleft()
            sum += n
            bridge.append(n)
        else:
            bridge.append(0)
        answer += 1
        if sum == 0 and not q:
            break

    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length, weight, truck_weights))

"""
먼저 다리를 deque로 다리의 길이만큼 0으로 초기화 해서 만든다.
sum 변수를 활용하여 다리에 있는 차들의 무게를 파악한다.
먼저 sum에 다리를 나가는 쪽을 의미하는 index를 빼면서 pop을 한다.
그 후 다리에 새로운 차가 들어할 수 있는 조건이 되면 그 차의 무게를 다리에 투입하고
아니라면 0을 넣는다. 다리의 현재 상태가 0이고 더이상 넣을 차가 없다면 반복문을 나간다.
(반복문은 반복 할수록 시간을 +1 한다.)
"""