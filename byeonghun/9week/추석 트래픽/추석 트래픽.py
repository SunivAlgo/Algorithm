from datetime import datetime, timedelta
from collections import Counter
def solution(lines):
    d = Counter()
    for line in lines:
        line = line.split()
        t = datetime.strptime(line[1], "%H:%M:%S.%f")
        period = timedelta(seconds=float(line[2][:-1]) - 0.001)
        diff = t - period
        psec = period.seconds

        while psec >= 0:
            strtime = str(diff.time()).split('.')
            print(strtime[0])
            if strtime[0] not in d:
                d[strtime[0]] = 1
            else:
                d[strtime[0]] += 1
            diff = diff + timedelta(seconds=1)
            psec -= 1
        
        if diff.microsecond + period.microseconds >= 1000000:
            strtime = str(diff.time()).split('.')
            print(strtime[0])
            if strtime[0] not in d:
                d[strtime[0]] = 1
            else:
                d[strtime[0]] += 1
        print()
    return d.most_common(n=1)[0][1]



print(solution([
    "2016-09-15 20:59:57.421 0.351s", 
    "2016-09-15 20:59:58.233 1.181s", 
    "2016-09-15 20:59:58.299 0.8s", 
    "2016-09-15 20:59:58.688 1.041s", 
    "2016-09-15 20:59:59.591 1.412s", 
    "2016-09-15 21:00:00.464 1.466s", 
    "2016-09-15 21:00:00.741 1.581s", 
    "2016-09-15 21:00:00.748 2.31s", 
    "2016-09-15 21:00:00.966 0.381s", 
    "2016-09-15 21:00:02.066 2.62s"]))