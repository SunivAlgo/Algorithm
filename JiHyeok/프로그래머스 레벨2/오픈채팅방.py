
def solution(record):
    answer = []
    userID_dic = dict()
    for i in range(len(record)):
        li_query = record[i].split()
        order = li_query[0]
        ID = li_query[1]
        

        if order == 'Enter' or order == 'Change':
            nickname = li_query[2]
            userID_dic[ID] = nickname
        
        record[i] = li_query


    Enter_korean = "님이 들어왔습니다."
    Leave_korean = "님이 나갔습니다."

    for query in record:
        if query[0] == 'Enter':
            answer.append(userID_dic[query[1]] + Enter_korean)
        elif query[0] == 'Leave':
            answer.append(userID_dic[query[1]] + Leave_korean)
        
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
'''
    1.  record의 명령이 Enter 나 Change 이면 딕셔너리에 key = ID , value = 닉네임 으로 저장해 놓는다.
    
    2.  다시 record를 순회하면서 Enter가 나오면 
        dic[ID]님이 들어왔습니다.

        Leave가 나오면
        dic[ID]님이 나갔습니다. 의 문자열을 answer에 저장시켜주면 됨

'''