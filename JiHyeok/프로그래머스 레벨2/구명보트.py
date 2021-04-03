from collections import deque
def solution(people, limit):
    weignt_now = 0
    answer = 0
    people.sort(reverse = True)
    people = deque(people)
    while people:
        weight_now = people.popleft()
        answer += 1
        if not people:
            return answer
        if weight_now + people[-1] <= limit:
            people.pop()
        weignt_now = 0

    return answer

print(solution([1,2,5,7,8,9],9))


'''
    처음에는 그저 sort를 해서 처음부터 넣으면 될 줄 알았음.
    근데 틀렸고,
    그래서 찾은게 내림차순으로 정렬하여 보트를 채워가는 것.
    ex ) people = 9,8,7,3,2,1     limit = 9
    1.  people[0] 9 + people[-1] 1> limit 이므로 people[0]만 보트에 태움 그리고 popleft
    2.  people[0] 8 + people[-1] 1 <= limit 이므로 people[0], people[-1] 둘다 pop
    3.  people[0] 7 + people[-1] 2 <= limit 이므로 people[0], people[-1] 둘다 pop
    4.  people[0] 3 에서 popleft를 해주면 더이상 원소가 없으므로 return answer.

'''