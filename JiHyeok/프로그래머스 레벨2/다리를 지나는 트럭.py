from collections import deque
def solution(bridge_length, weight, truck_weights):
    k = 0
    weightsum = 0
    time = 0
    bridge = [0] * bridge_length
    bridge = deque(bridge)
    wait = deque(truck_weights)
   
    while wait:
        time += 1
        weightsum -= bridge.popleft()
        x = 0
        if wait[0] + weightsum <= weight:
            x = wait[0]
            k = x
            weightsum += wait.popleft()
        bridge.append(x) 
            
    while k in bridge:
        time += 1
        bridge.popleft()
    return time
print(solution(2,10,[7,4,5,6]	))