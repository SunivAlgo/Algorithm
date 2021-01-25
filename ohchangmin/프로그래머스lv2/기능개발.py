import math

def solution(progresses, speeds):
    answer = []
    
    for i in range(0, len(progresses)):
        if progresses[i] < 100:
            n = math.ceil((100 - progresses[i]) / speeds[i])
            count = 0
            for j in range(i, len(progresses)):
                progresses[j] += speeds[j] * n
            for j in range(i, len(progresses)):
                if progresses[j] >= 100:
                    count += 1
                else:
                    break
            answer.append(count)

    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]	
print(solution(progresses, speeds))

"""
이 문제를 풀때 단순하게 1일이 증가할때 마다 progresses에 speeds를
더해주는 방법으로 하면 문제를 풀 수 있을것 같았다. 하지만 첫번째로
나오는 100이 아닌 progresses에 필요한 기간을 구하고 그 기간 만큼을
모든 progresses에 더해준 다음 100이상인 progresses를 찾아내는 방식이 
더 효율적일 것 같아서 후자의 방법을 통해 문제 풀이를 진행하였다.
""" 