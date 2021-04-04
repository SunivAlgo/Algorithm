from collections import deque

def solution(jobs):
    answer = 0
    lenjobs = len(jobs)
    jobs.sort(key = lambda x : (x[0], x[1]))
    jobs = deque(jobs)
    time = jobs[0][0]
    l = []
    while jobs or l:
        work = jobs.popleft()
        if time >= work[0]: 
            time += work[1]
            answer += time - work[0]
        else: # 작업이 한참 뒤에 있을시
            time = work[0] + work[1]
            answer += work[1]
        while jobs and jobs[0][0] <= time:
            l.append(jobs.popleft())
        if l:
            l.sort(key = lambda x: x[1], reverse = True)
            jobs.appendleft(l.pop())
    return answer // lenjobs

print(solution([[0, 1], [1000, 1000]]))