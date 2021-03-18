def solution(lines):
    answer = 0
    times = []
    for line in lines:
        line_split = line.split()
        time_split = line_split[1].split(':')
        # 시간을 전부 밀리초로 바꾼다. 초단위로 안한 이유는 나중에 0.999를 더하면 소수점 더하기를 하기 때문에 이상한 값이 나올수 있어서 정수로 만들어 주고 싶어서이다
        end_time = float(time_split[0]) * 3600000 + float(time_split[1]) * 60000 + float(time_split[2]) * 1000      
        start_time = end_time - (float(line_split[2][:-1]) * 1000) + 1
        times.append([start_time, end_time])

    times.sort(key= lambda x : x[1])    #시작시간과 끝나는 시간이 저장된 배열을 끝나는 시간 기준으로 정렬한다.
    
    for i in range(len(times)):
        cnt = 0
        start = times[i][1]     #1초 구간을 선정한다.
        end = start + 999   
        for j in range(i, len(times)):       
            if times[j][0] <= end:      #정렬을 이미 해놓았기 때문에 이 조건문을 사용하면 그 구간안에 요소가 있는지 확인이 가능하다.
                cnt += 1
        if answer < cnt:
            answer = cnt
    return answer

lines = [
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
print(solution(lines))