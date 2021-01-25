from collections import deque
def solution(progresses, speeds):
    answer = []
    days = []
    count = 0
    
    queue = deque()

    for i in range(0,len(progresses)):
        day = (100-progresses[i])/speeds[i]
        if day - int(day) > 0:
            day = int(day) + 1
        days.append(int(day))
    
    for i in days:
        queue.append(i)
        if i > queue[0]:
            while(queue[0] != i):
                queue.popleft()
                count += 1
            answer.append(count) 
            count = 0
         
    
    answer.append(len(queue))

    return answer

print(solution([91,97,90,95,94],[1,1,1,1,1]))