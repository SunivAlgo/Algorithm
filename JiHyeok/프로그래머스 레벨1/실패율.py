def fail(stages,N):
    count = 0
    temp = 0
    sum = 0
    count_list = []
    fail_list = []
    stages.sort()
    for i in range(1,N+2):
        for j in range(0,len(stages)):
            if i < stages[j]:
                break
            if i == stages[j]:
                count += 1
        count_list.append(count)
        count = 0
    

    for i in range(0,len(count_list)-1):
        for j in range(i, len(count_list)):
            sum += count_list[j]
        if sum!=0:
            temp = count_list[i] / sum
        fail_list.append(temp)
        temp = 0
        sum = 0
    
    return fail_list
def solution(N, stages):
    answer = []
    fail_list = []

    fail_list = fail(stages,N)
    for i in range (0,len(fail_list)):
        answer.append(fail_list.index(max(fail_list))+1)
        fail_list[fail_list.index(max(fail_list))] = -1
    return answer

'''
   
   1. stage 리스트 정렬하여 각 원소마다 실패율을 구한다음 실패율 리스트 생성
   2. 실패율의 max 값의 index를 구하여 1 ~ N의 원소가 들어있는 리스트에 해당하는 값 선택 
'''