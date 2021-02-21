def createDic(record):
    log, dic=[], {}
    for i in record:
        rec=i.split()
        if rec[0]!='Change': log.append([rec[0], rec[1]])

        #dic: key= uid, value=nickname
        if rec[0]=='Enter': dic[rec[1]]=rec[2]
        elif rec[0]=='Change': dic[rec[1]]=rec[2]

    return log, dic

def solution(record):
    answer = []
    chat_log, nick_dic = createDic(record)
    for i in chat_log:
        if i[0]=='Enter':
            answer.append(nick_dic[i[1]]+'님이 들어왔습니다.')
        else:
            answer.append(nick_dic[i[1]]+'님이 나갔습니다.')

    return answer


#https://blog.naver.com/leemyo_/222249839216



"""
in: "[닉네임]님이 들어왔습니다."
out: "[닉네임]님이 나갔습니다."

닉변 method
1. 나왔다 들어오기
2. 채팅방에서 바꾸기

닉네임을 변경할 때는 기존에 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경
기존 채팅방에 남아있던 이 사람의 흔적도 다 변함
채팅방은 중복 닉네임을 허용

채팅방 기록이 담긴 문자열 배열 record가 매개변수
모든 기록이 처리된 후, 최종적으로 방을 개설한 사람이 보게 되는 메시지를 문자열 배열 형태로 return

record(1-10만)
첫 단어는 Enter, Leave, Change 중 하나
각 단어는 공백으로 구분
알파벳 대문자, 소문자, 숫자로만 이루어져있다.
유저 아이디와 닉네임은 알파벳 대문자, 소문자를 구별
유저 아이디와 닉네임의 길이는 1 이상 10 이하
"""
