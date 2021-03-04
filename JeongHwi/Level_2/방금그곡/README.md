# 방금 그 곡

[출처 - Programmers](https://programmers.co.kr/learn/courses/30/lessons/17683)

###### 문제 설명

라디오를 자주 듣는 네오는 라디오에서 방금 나왔던 음악이 무슨 음악인지 궁금해질 때가 많다. 그럴 때 네오는 다음 포털의 '방금그곡' 서비스를 이용하곤 한다. 방금그곡에서는 TV, 라디오 등에서 나온 음악에 관해 제목 등의 정보를 제공하는 서비스이다.

네오는 자신이 기억한 멜로디를 가지고 방금그곡을 이용해 음악을 찾는다. 그런데 라디오 방송에서는 한 음악을 반복해서 재생할 때도 있어서 네오가 기억하고 있는 멜로디는 음악 끝부분과 처음 부분이 이어서 재생된 멜로디일 수도 있다. 반대로, 한 음악을 중간에 끊을 경우 원본 음악에는 네오가 기억한 멜로디가 들어있다 해도 그 곡이 네오가 들은 곡이 아닐 수도 있다. 그렇기 때문에 네오는 기억한 멜로디를 재생 시간과 제공된 악보를 직접 보면서 비교하려고 한다. 다음과 같은 가정을 할 때 네오가 찾으려는 음악의 제목을 구하여라.

- 방금그곡 서비스에서는 음악 제목, 재생이 시작되고 끝난 시각, 악보를 제공한다.
- 네오가 기억한 멜로디와 악보에 사용되는 음은 C, C#, D, D#, E, F, F#, G, G#, A, A#, B 12개이다.
- 각 음은 1분에 1개씩 재생된다. 음악은 반드시 처음부터 재생되며 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생된다. 음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다.
- 음악이 00:00를 넘겨서까지 재생되는 일은 없다.
- 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
- 조건이 일치하는 음악이 없을 때에는 “`(None)`”을 반환한다.

### 입력 형식

입력으로 네오가 기억한 멜로디를 담은 문자열 `m`과 방송된 곡의 정보를 담고 있는 배열 `musicinfos`가 주어진다.

- `m`은 음 `1`개 이상 `1439`개 이하로 구성되어 있다.
- musicinfos는 100개 이하의 곡 정보를 담고 있는 배열로, 각각의 곡 정보는 음악이 시작한 시각, 끝난 시각, 음악 제목, 악보 정보가 `,`로 구분된 문자열이다.
  - 음악의 시작 시각과 끝난 시각은 24시간 `HH:MM` 형식이다.
  - 음악 제목은 '`,`' 이외의 출력 가능한 문자로 표현된 길이 `1` 이상 `64` 이하의 문자열이다.
  - 악보 정보는 음 `1`개 이상 `1439`개 이하로 구성되어 있다.

### 출력 형식

조건과 일치하는 음악 제목을 출력한다.

### 입출력 예시

| m                  | musicinfos                                                 | answer  |
| ------------------ | ---------------------------------------------------------- | ------- |
| "ABCDEFG"          | ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]  | "HELLO" |
| "CC#BCC#BCC#BCC#B" | ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]   | "FOO"   |
| "ABC"              | ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"] | "WORLD" |

### 설명

첫 번째 예시에서 HELLO는 길이가 7분이지만 12:00부터 12:14까지 재생되었으므로 실제로 CDEFGABCDEFGAB로 재생되었고, 이 중에 기억한 멜로디인 ABCDEFG가 들어있다.
세 번째 예시에서 HELLO는 C#DEFGABC#DEFGAB로, WORLD는 ABCDE로 재생되었다. HELLO 안에 있는 ABC#은 기억한 멜로디인 ABC와 일치하지 않고, WORLD 안에 있는 ABC가 기억한 멜로디와 일치한다.

[해설 보러가기](http://tech.kakao.com/2017/11/14/kakao-blind-recruitment-round-3/)

### Code

```python
def timeGet(start,end):
    start_h, start_m = start.split(":")
    end_h, end_m = end.split(":")
    minute = int(end_m) - int(start_m)
    hour = int(end_h) - int(start_h)
    minute+=hour*60
    return minute    
import re
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

import re
def solution(m,musicinfos):
    ans = []
    for infos in musicinfos:
        start,end,name,melody = infos.split(',')
        time = timeGet(start,end)
        melodyList = getMelodyList(melody)
        totalList = ""
        for i in range(time):
            totalList+=melodyList[i%len(melodyList)]
        # print("이전 :",totalList)
        totalList = totalList.replace(m+"#","-")
        totalList = totalList.replace(m,"!")
        # if totalList.find(m) >= 0 :
        #     if totalList.find(m+"#") >= 0:
        #         continue
        #     # print(totalList,m,tkotalList.find(m))
        #     ans.append((name,time))
        # print("후 ",totalList)
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
```

### Solution

진짜 문제 이해하는게 제일 어려운 문제

`timeGet` 함수는 걸린 시간을 minute으로 환산한 시간을 리턴한다.

`getMelodyList` 함수는 melody를 C,C#,B,D,E,F. .. 이런식으로 나눈 리스트를 리턴

`timeGet` 함수에서 나온 시간만큼 For문을 수행한다. `totalList`에는 시간동안 들은 멜로디를 한줄로 모아둔 list

그리고 `m+"#"` 과 match되는 단어를 먼저 "-" 로 `replace` 시키는데, 이는 `ABC` 가 `ABC#`도 동일하다고 이미 판단을 하기 때문에 예외처리를 한다.

처리 후, `m` 과 match되는 단어를 "!" 로 변경시켜 "!" 를 찾아 `(name,time)` 으로 `ans` 에 삽입한다.

그리고 `ans`를 시간순으로 정렬하여 가장 큰 시간의 노래이름을 반환한다.

`+9`