from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    while queue:
        if queue[0] == max(queue):
            if location <= 0:
                answer += 1
                break
            else :
                queue.popleft()
                location -= 1
                answer += 1
        else :
            if location <= 0:
                queue.append(queue.popleft())
                location += len(queue) - 1
            else :
                queue.append(queue.popleft())
                location -= 1
        

    return answer

print(solution([1,1,9,1,1,1],0))

'''
    1. queue[0]이 max값일 때 프린트가 되므로 queue[0]이 max값인지 판단하는 동시에
       location에 해당하는 원소인지를 알아야 한다
    
    2.  queue[0]이 max값일 때
        a.  location == 0 --> print해주고 반복문 break (정답이 나왔으므로)
        b.  location != 0 --> print해주고 location -= 1

    3.  queue[0]이 max값이 아닐 때
        a.  location == 0 --> queue[0]의 값이 제일 뒤로 가야 하므로 location = len(queue) - 1
        b.  location != 0 --> queue[0]의 제일 뒤에 가면서 그저 location -= 1

    4. answer 값은 print 횟수를 나타내는 값이므로 queue[0]이 max일 때만 answer += 1
'''