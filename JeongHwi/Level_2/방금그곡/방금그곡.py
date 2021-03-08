def timeGet(start,end):
    start_h, start_m = start.split(":")
    end_h, end_m = end.split(":")
    minute = int(end_m) - int(start_m)
    hour = int(end_h) - int(start_h)
    minute+=hour*60
    return minute    

def getMelodyList(melody):
    ml = []
    me = ""
    melodylen = len(melody)
    for i in range(melodylen):
        if melody[i] == "#":
            ml.append(me)
            me = ""
            continue
        me += melody[i]
        if i != melodylen-1:
            if melody[i+1] == "#" :
                me += melody[i+1]
            else:
                ml.append(me)
                me=""
        else:
            ml.append(melody[i])
    return ml

def solution(m,musicinfos):
    ans = []
    for infos in musicinfos:
        start,end,name,melody = infos.split(',')
        time = timeGet(start,end)
        melodyList = getMelodyList(melody)
        print(melodyList)
        totalList = ""
        for i in range(time):
            totalList+=melodyList[i%len(melodyList)]
        totalList = totalList.replace(m+"#","-")
        totalList = totalList.replace(m,"!")
        if totalList.find("!") >= 0:
            ans.append((name,time))
    if not ans:
        return "(None)"
    ans.sort(key=lambda x:-x[1])
    return ans[0][0]


print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CCB",["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]))