import heapq
'''
1. 각 작업의 요청부터 종료까지 걸린 시간의 평균이 제일 작아야 함
-> 하드디스크에 넣을 수 있는 후보 중에서 제일 수행시간이 작은 것을 먼저 수행하면 해결

2. 하드디스크가 할 일이 없을 때가 나온다. ex) [0,3] [4,1], [5,3]
이럴때는 그냥 [4,1]을 처리
'''
def solution(jobs):
    answer = 0
    jobs_size = len(jobs) ## jobs size 저장
    time_now = 0 ## 현재 시간을 나타내는 변수
    jobs.sort(key=lambda x : (x[0],x[1])) ## 1. 시간순 2. 작업 수행시간순 정렬

    while(jobs): ## jobs가 존재하는 동안 계속
        heap = []
        for i in range(0,len(jobs)):
            if jobs[i][0] > time_now: ##jobs[i][0](시간)이 time_now보다 크면 2.번인 경우이다.
                break
            heapq.heappush(heap,(jobs[i][1], i)) ## 밀린 작업들을 모두 작업시간순으로 힙에 넣음
        if heap: ## 힙이 존재한다는 것 = 밀린 작업이 있다는 것
            index = heapq.heappop((heap))[1]
            answer += ((time_now - jobs[index][0]) + jobs[index][1])
            time_now += jobs[index][1]
        else: ## 힙이 없다는 것 = 밀린 작업이 없어서 jobs중에 첫번째 작업을 해야한다는 뜻
            index = 0
            answer += jobs[index][1]
            time_now = (jobs[index][0] + jobs[index][1])
        del(jobs[index]) ## 작업한 프로세스는 삭제
    answer //= jobs_size

    return answer

print(solution([[1, 3], [1, 9], [2, 6]]))
##print(solution([[0, 3], [1, 9], [2, 6]]))
##print(solution([[0, 2], [3, 1], [5, 6]]))
##print(solution([[1,2],[1,3],[2,5],[3,6],[5,7],[100,13]]))