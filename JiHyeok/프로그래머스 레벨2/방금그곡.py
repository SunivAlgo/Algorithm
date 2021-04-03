# flake8: noqa
def solution(m, musicinfos):
    answer = ''
    new_m = ''

    ##  m 에서 #이 붙어있는 계이름은 소문자로 변경
    for i in range(len(m)):
        if m[i] == '#':
            continue
        if i == len(m) - 1:
            new_m += m[i]
            break
        if m[i+1] == '#':
            new_m += m[i].lower()
            continue
        new_m += m[i]

    ##  dic_song 이라는 dict에는
    ##  title : [start_time,end_time,time,songinfo]
    dic_song = dict()
    musicinfos = [musicinfo.split(',') for musicinfo in musicinfos]
    
    for li in musicinfos:
        end_time = int(li[1][:2]) * 60 + int(li[1][3:])
        start_time = int(li[0][:2]) * 60 + int(li[0][3:])
        time = end_time - start_time
        title = li[2]
        songinfo = ''
        for i in range(len(li[3])):
            if li[3][i] == '#':
                continue
            if i == len(li[3]) - 1:
                songinfo += li[3][i]
                break
            if li[3][i+1] == '#':
                songinfo += li[3][i].lower()
                continue
            songinfo += li[3][i]
        li[3] = songinfo

        while len(li[3]) < time:
            li[3] += songinfo
        songinfo = li[3][:time + 1]
        
        dic_song[title] = [start_time, end_time, time, songinfo]
    
    answer_candidate = []
    for key in dic_song.keys():
        if new_m in dic_song[key][3]:
            answer_candidate.append(key)
    
    if not answer_candidate:
        return '(None)'
    
    if len(answer_candidate) == 1 :
        return answer_candidate[0]
    
    answer_candidate.sort(key = lambda title : (dic_song[title][2], -dic_song[title][0]))
    
    answer = answer_candidate[-1]

    return answer

'''

    1.  m에서 #이 붙은 음들은 모두 소문자로 변경.
    
    2.  [시작시간,끝시간,총시간,악보정보]를 갖고있는 '곡제목'을 key로 하는 딕셔너리 dic_song을 만들었음
        --악보정보도 m 과 마찬가지로 #이 붙은 음들은 모두 소문자로 변경하였음
    
    3.  dic_song.keys()로 각 곡의 악보정보를 참조하여 정답후보군들을 추렸음

    4.  정답후보의 개수 = 0 --> none
                         1 --> 정답
                         2 --> 다음 조건절로 넘어감

    5.  조건절을 적용시키기 위해 answer_candidate(정답후보)의 key값들을 정렬시켰는데
        1)  재생시간 (오름차순)
        2)  시작시간 (내림차순)
        정렬하여 answer_candidate[-1] 이 정답이 되게 하였음

'''