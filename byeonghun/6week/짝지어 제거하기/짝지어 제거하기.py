from collections import deque
def solution(s):
    sq = deque(list(s))
    temp = deque(sq.popleft())
    while sq:
        while temp:
            if sq and sq[0] == temp[-1]:
                temp.pop()
                sq.popleft()
            else: break
        if sq:
            temp.append(sq.popleft())
    if temp :
        return 0
    else:
        return 1