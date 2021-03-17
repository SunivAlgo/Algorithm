
def convert_Melody(melody):
    melody = melody.replace("C#","1")
    melody = melody.replace("A#","2")
    melody = melody.replace("D#","3")
    melody = melody.replace("F#","4")
    melody = melody.replace("G#","5")
    return melody

def getTime(start,end):
    start_hour,start_minute = map(int,start.split(":"))
    end_hour,end_minute =  map(int,end.split(":"))
    return (end_hour-start_hour)*60 + (end_minute-start_minute)
def solution(m,musicinfo):
    m = convert_Melody(m)
    ans = []
    for musics in musicinfo:
        start,end,name,melody = musics.split(",")
        time = getTime(start,end)
        melody_conv = convert_Melody(melody)
        mlen = len(melody_conv)
        ans_melody = ""
        if time == 0:
            continue
        for i in range(time):
            ans_melody += melody_conv[i%mlen]

        if m in ans_melody:
            ans.append((name,time))
    ans.sort(key=lambda x:-x[1])
    if ans:
        return ans[0][0]
    else:
        return "(None)"

print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
