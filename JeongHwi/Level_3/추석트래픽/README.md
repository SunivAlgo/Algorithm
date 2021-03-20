# 추석 트래픽

###### 문제 설명

## 추석 트래픽

이번 추석에도 시스템 장애가 없는 명절을 보내고 싶은 어피치는 서버를 증설해야 할지 고민이다. 장애 대비용 서버 증설 여부를 결정하기 위해 작년 추석 기간인 9월 15일 로그 데이터를 분석한 후 초당 최대 처리량을 계산해보기로 했다. **초당 최대 처리량**은 요청의 응답 완료 여부에 관계없이 임의 시간부터 1초(=1,000밀리초)간 처리하는 요청의 최대 개수를 의미한다.

### 입력 형식

- `solution` 함수에 전달되는 `lines` 배열은 **N**(1 ≦ **N** ≦ 2,000)개의 로그 문자열로 되어 있으며, 각 로그 문자열마다 요청에 대한 응답완료시간 **S**와 처리시간 **T**가 공백으로 구분되어 있다.
- 응답완료시간 **S**는 작년 추석인 2016년 9월 15일만 포함하여 고정 길이 `2016-09-15 hh:mm:ss.sss` 형식으로 되어 있다.
- 처리시간 **T**는 `0.1s`, `0.312s`, `2s` 와 같이 최대 소수점 셋째 자리까지 기록하며 뒤에는 초 단위를 의미하는 `s`로 끝난다.
- 예를 들어, 로그 문자열 `2016-09-15 03:10:33.020 0.011s`은 "2016년 9월 15일 오전 3시 10분 **33.010초**"부터 "2016년 9월 15일 오전 3시 10분 **33.020초**"까지 "**0.011초**" 동안 처리된 요청을 의미한다. **(처리시간은 시작시간과 끝시간을 포함)**
- 서버에는 타임아웃이 3초로 적용되어 있기 때문에 처리시간은 **0.001 ≦ T ≦ 3.000**이다.
- `lines` 배열은 응답완료시간 **S**를 기준으로 오름차순 정렬되어 있다.

### 출력 형식

- `solution` 함수에서는 로그 데이터 `lines` 배열에 대해 **초당 최대 처리량**을 리턴한다.

### 입출력 예제

#### 예제1

- 입력: [
  "2016-09-15 01:00:04.001 2.0s",
  "2016-09-15 01:00:07.000 2s"
  ]
- 출력: 1

#### 예제2

- 입력: [
  "2016-09-15 01:00:04.002 2.0s",
  "2016-09-15 01:00:07.000 2s"
  ]
- 출력: 2
- 설명: 처리시간은 시작시간과 끝시간을 **포함**하므로
  첫 번째 로그는 `01:00:02.003 ~ 01:00:04.002`에서 2초 동안 처리되었으며,
  두 번째 로그는 `01:00:05.001 ~ 01:00:07.000`에서 2초 동안 처리된다.
  따라서, 첫 번째 로그가 끝나는 시점과 두 번째 로그가 시작하는 시점의 구간인 `01:00:04.002 ~ 01:00:05.001` 1초 동안 최대 2개가 된다.

#### 예제3

- 입력: [
  "2016-09-15 20:59:57.421 0.351s",
  "2016-09-15 20:59:58.233 1.181s",
  "2016-09-15 20:59:58.299 0.8s",
  "2016-09-15 20:59:58.688 1.041s",
  "2016-09-15 20:59:59.591 1.412s",
  "2016-09-15 21:00:00.464 1.466s",
  "2016-09-15 21:00:00.741 1.581s",
  "2016-09-15 21:00:00.748 2.31s",
  "2016-09-15 21:00:00.966 0.381s",
  "2016-09-15 21:00:02.066 2.62s"
  ]
- 출력: 7
- 설명: 아래 타임라인 그림에서 빨간색으로 표시된 1초 각 구간의 처리량을 구해보면 `(1)`은 4개, `(2)`는 7개, `(3)`는 2개임을 알 수 있다. 따라서 **초당 최대 처리량**은 7이 되며, 동일한 최대 처리량을 갖는 1초 구간은 여러 개 존재할 수 있으므로 이 문제에서는 구간이 아닌 개수만 출력한다.
  ![Timeline](figure/README/chuseok-01-v5.png)

[해설 보러가기](http://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/)



### Code

```python
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
```



### Solution

창민이의 답을 참고 (`+2`)

우선 start와 end 시간을 `datetime` 으로 변환해서 하나의 배열에 저장한다.

그리고 end + 999millisecond 만큼 더한만큼이 Check 구간이다.

여기서 가장 주의 있게 생각해야할 점은 **1 초 구간** 이라는 점이다.

1초 구간안에 가장 많은 트래픽이 있는 구간을 찾는 것이라는 것이다.

현재는 end 지점으로 정렬되어있다. 따라서 `end+999` 지점보다 `start` 지점이 작은 부분에 대해서만 찾으면된다.

`시간 구간` 이라는 말이 중요한 것 같다. `i-1` 부분을 체크하지 않는 이유는 `i-1` 은 이미 자신의 최대 구간을 체크했기 때문.

