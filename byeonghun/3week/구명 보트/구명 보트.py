from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse= True)
    speople = deque(people)
    while speople:
        if len(speople) == 1:
            answer += 1
            break
        if speople[0] + speople[-1] > limit:
            answer += 1
            speople.popleft()
            continue
        onboat = speople.pop() + speople.popleft()
        while True:
            if not speople:
                answer += 1
                break
            if onboat == limit or onboat + speople[-1] > limit:
                answer += 1
                break
            else:
                onboat += speople.pop()
    return answer

print(solution([40, 40, 40, 40], 100))