from datetime import timedelta

def timeConvert(time,proces):
    hour,minute,m_second = time.split(":")
    hour,minute = map(int,[hour,minute])
    m_second = int(m_second.replace(".",""))
    m_proces = int(float(proces)*1000)

    complete = timedelta(days=15,hours=hour,minutes=minute,milliseconds=m_second+1)
    start = complete - timedelta(milliseconds=m_proces)
    complete -= timedelta(milliseconds=1)
    return start,complete

def calc_Process(timeList,tlen):
    max_count = 0
    #timeList는 시작순서로 정해져있음
    for i in range(tlen):
        count = 0
        end_ = timeList[i][1] + timedelta(milliseconds=999)
        for j in range(i,tlen):
            if timeList[j][0] <= end_:
                count+=1
        max_count = max(count,max_count)
    
    return max_count
def solution(lines):
    process_time = []
    for l in lines:
        _,time,proces = l.split()
        proces = proces[:-1]
        start,complete = timeConvert(time,proces)
        process_time.append((start,complete))
    # process_time.sort(key=lambda x:x[1])
    tlen = len(process_time)
    if tlen == 1:
        return 1
    return calc_Process(process_time,tlen)

# print(solution(["2016-09-15 01:00:04.001 2.0s","2016-09-15 01:00:07.000 2s"]))

# print(solution(["2016-09-15 01:00:04.002 2.0s","2016-09-15 01:00:07.000 2s"]))

print(solution(["2016-09-15 20:59:57.421 0.351s","2016-09-15 20:59:58.233 1.181s",
                "2016-09-15 20:59:58.299 0.8s","2016-09-15 20:59:58.688 1.041s",
                "2016-09-15 20:59:59.591 1.412s","2016-09-15 21:00:00.464 1.466s",
                "2016-09-15 21:00:00.741 1.581s","2016-09-15 21:00:00.748 2.31s",
                "2016-09-15 21:00:00.966 0.381s","2016-09-15 21:00:02.066 2.62s"]))
