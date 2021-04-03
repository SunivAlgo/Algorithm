import heapq
def solution(jobs):
    answer = 0
    jobs_size = len(jobs)
    time_now = 0
    jobs.sort(key=lambda x : (x[0],x[1]))

    while(jobs):
        heap = []
        for i in range(0,len(jobs)):
            if jobs[i][0] > time_now:
                break
            heapq.heappush(heap,(jobs[i][1], i))
        if heap:
            index = heapq.heappop((heap))[1]
            answer += ((time_now - jobs[index][0]) + jobs[index][1])
            time_now += jobs[index][1]
        else:
            index = 0
            answer += jobs[index][1]
            time_now = (jobs[index][0] + jobs[index][1])
        del(jobs[index])
    answer //= jobs_size

    return answer

print(solution([[1, 3], [1, 9], [2, 6]]))
##print(solution([[0, 3], [1, 9], [2, 6]]))
##print(solution([[0, 2], [3, 1], [5, 6]]))
##print(solution([[1,2],[1,3],[2,5],[3,6],[5,7],[100,13]]))