people = [70,50,80,50]
limit = 100

from collections import deque
def solution(people,limit):
    people.sort(reverse=True)
    people = deque(people)
    boat = 0
    while people:
        if people[0] < limit//2:
            people.popleft()
            if people:
                people.pop()
            boat+=1
            continue
        if people[0] + people[-1] > limit:
            people.popleft()
            boat += 1
        elif people[0] + people[-1] <= limit:
            people.popleft()
            if people:
                people.pop()
            boat+=1
    return boat
     
print(solution(people,limit))