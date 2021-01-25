from collections import deque

priorities = [2, 1, 3, 2]
location = 2

def solution(priorities, location):
    answer = 1
    ind = deque([])
    queue = deque([])

    for i in range(0, len(priorities)):
        ind.append(i)
    for i in priorities:
        queue.append(i)

    while True:
        num = queue.popleft()
        now = ind.popleft()
        if num == max(priorities):
            if now == location:
                break
            else:
                answer+=1
                priorities[now] = 0
        else:
            queue.append(num)
            ind.append(now)
    return answer

solution(priorities, location)

"""
인덱스와 데이터를 담는 큐를 하나 씩 생성한다
리스트로 하지 않고 따로 큐를 생성한 이유는 첫번째 
데이터의 제거가 리스트보다 효율적이기 때문에 큐를 
사용하였다. 첫 번째 데이터가 가장 큰 수이고 구하고자
하는 인덱스가 일치할 때 반복문을 나가고 아닐 시에는
값을 +1, 우선순위를 0으로 바꿔준다. 가장 큰수가 아닐
시에는 빼낸 값과 인덱스를 다시 큐에 넣어준다.
"""
