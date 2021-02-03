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

'''
    1.  첫번째 for문에서 각 progress마다 필요한 day수를 구했습니다.
    2.  두번쨰 for문은 day리스트로 출시일이 같은 progress를 구하는데,
        ex) 4,6,5,7,8 이 day 리스트면
        4를 일단 queue에 넣고 queue[0]과 비교. 4 == queue[0] 이니 아무일도 일어나지 않음
        6을 queue에 넣음, queue[0]과 비교. 6 > queue[0] == 4 이니 queue[0]이 6이 아닐동안 pop해주면서 count++
        이렇게 진행하면, [1,2]를 얻는데, [7,8]을 count한 수를 배열에 넣어주기 위해 for문이 끝나면 queue의 길이를 세준다.
'''