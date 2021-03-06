import re 
import datetime
from collections import deque

def solution(m, musicinfos):
    answer = []
    sequence = 0
    m = re.findall(r"([A-G]#?)",m)
    for i in range(len(m)):
        if len(m[i]) == 2:
            m[i] = m[i][0].lower()
    m = "".join(m)

    for musicinfo in musicinfos:
        mlist = musicinfo.split(',')

        name = mlist[2]
        fullmusic = re.findall(r"([A-G]#?)",mlist[3])

        for i in range(len(fullmusic)):
            if len(fullmusic[i]) == 2:
                fullmusic[i] = fullmusic[i][0].lower()

        start = datetime.datetime.strptime(mlist[0], '%H:%M')
        fin = datetime.datetime.strptime(mlist[1], '%H:%M')
        result = fin - start
        music_len = result.seconds // 60
        if music_len > len(fullmusic):
            i = 0
            temp = len(fullmusic)
            while music_len > len(fullmusic):
                fullmusic.append(fullmusic[i % temp])
                i += 1
        elif music_len < len(fullmusic):
            while music_len < len(fullmusic):
                fullmusic.pop()

        if m in "".join(fullmusic):
            answer.append([music_len, name, sequence])
            sequence += 1

    if not answer:
        return "(None)"
    answer.sort(key= lambda x: (x[0],x[2]))
    return answer[0][1]

print(solution(	"CCB", ["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]))