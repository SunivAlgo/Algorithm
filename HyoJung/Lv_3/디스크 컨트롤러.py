import heapq

def solution(jobs):
    answer, now, len_jobs = 0, 0, len(jobs)
    h, v, cnt = [], [0]*len_jobs, 0
    
    while cnt!=len_jobs:
        for i,x in enumerate(jobs):
            if sum(v)==len_jobs: break
            if x[0]<=now and v[i]==0:
                heapq.heappush(h,[x[1],x[0]])
                v[i]=1
        if len(h)>0:
            job = heapq.heappop(h)
            now+=job[0]
            answer += (now-job[1])
            cnt+=1
        else:
            now+=1
            
    return int(answer/len_jobs)

# https://blog.naver.com/leemyo_/222297395599