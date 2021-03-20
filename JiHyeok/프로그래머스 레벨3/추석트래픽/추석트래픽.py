

def solution(lines):
    answer = 0
    
    for i in range(len(lines)):
        lines[i] = lines[i].split(' ')
        lines[i][1] = lines[i][1].split(':')

        lines[i][1] = int((int(lines[i][1][0]) * 3600 + int(lines[i][1][1])  * 60 + float(lines[i][1][2])) * 1000)
        
        lines[i][2] = int(float(lines[i][2][:-1]) * 1000)

        lines[i][0] = lines[i][1] - lines[i][2] + 1
    
    ######## lines 초기화
    ## print(lines)

    for i in range(len(lines)):
        check_start_time = lines[i][1] ## i번째 line 의 end 타임
        check_end_time = check_start_time + 1000 ## end 타임에 1초 더한 시각
        count = 0
        for j in range(i,len(lines)):
            if lines[j][0] < check_end_time:
                count += 1
        answer = max(count,answer)

    
    
    return answer

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
"2016-09-15 21:00:02.066 2.62s"
]))

##print(solution(["2016-09-15 00:00:00.000 3s"]))
##print(solution(	["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))