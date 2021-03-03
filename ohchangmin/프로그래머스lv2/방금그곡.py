def solution(m, musicinfos):
    answer = ''
    max_time = 0
    for i in musicinfos:
        info = i.split(',')
        start = int(info[0][0:2]) * 60 + int(info[0][3:5])
        end = int(info[1][0:2]) * 60 + int(info[1][3:5])
        title = info[2]
        music = info[3]

        if start > end:
            end = 24 * 60        
        time = end - start

        melody = ""
        ind = 0
        for i in range(time):
            melody += music[ind]
            ind += 1
            if ind == len(music):
                ind = 0
            if music[ind] == '#':
                melody += music[ind]
                ind += 1
            if ind == len(music):
                ind = 0

 
        for i in range(0, len(melody) - len(m)+1):
            if melody[i] == '#':
                continue

            if m == melody[i:i+len(m)] and max_time < time:
                if i+len(m) < len(melody) and melody[i+len(m)] == '#':
                    continue
                answer = title
                max_time = time
    if answer == '':
        return "(None)"
    return answer


m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))
m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m, musicinfos))
m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))
m = "A#"
musicinfos = ["13:00,13:02,HAPPY,B#A#"]
print(solution(m, musicinfos))


'''
처음에 생각했던 방법은 A# 같은 경우는 a F#같은 경우는 f로 변환하여
문제를 푸는 방식도 생각하였으나 바꾸는 과정에서 시간이 조금 더 걸릴 것
같아서 그냥 인덱스를 잘 참조하여 풀기로 하였다. 하지만 바꿔서 하는 방식이
훨씬 쉬운 과정인 것 같다.

먼저 걸린 시간을 구한 후 걸린 시간에 따른 멜로디를 만들었다.
이제 m이 멜로디에 있는지 확인하는 작업이 필요한데 #유무로 인하여
단순히 m in melody 같은 형식으로 구할 수 없었다. 그래서 일일히 멜로디의 인덱스를
참조하면서 m과 같은 부분이 있는지 확인하는 작업을 진행하였다. 
'''