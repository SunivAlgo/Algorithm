from collections import deque

def solution(people, limit):
    answer = 0
    dq_people = deque(sorted(people))

    while len(dq_people) != 0:
        p = dq_people.pop()
        if len(dq_people) != 0 and dq_people[0] + p <= limit:
            dq_people.popleft()
        answer += 1

    return answer

people=[70, 50, 80, 50]
limit=100

print(solution(people, limit))

'''
people를 오름차순으로 정렬된 큐로 구성 큐가 비어있을때까지 반복문
을 돌린다. 가장 큰수를 pop을 하고 큐의 가장 작은수와의 합이 리미트 
이하이면 가장 작은 수도 pop을 한다. 반복문 돌아갈때마다 answer+1
'''