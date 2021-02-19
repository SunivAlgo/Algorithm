def solution(record):
    temp = []
    users = {}
    for command in record:
        split_command = command.split(' ')
        action = split_command[0]
        id = split_command[1]
        if action != 'Leave':
            nick_name = split_command[2]

        if action == 'Enter':
            users[id] = nick_name
            temp.append([id, "님이 들어왔습니다."])
        elif action == 'Leave':
            temp.append([id, "님이 나갔습니다."])
        elif action == 'Change':
            users[id] = nick_name

    answer = []
    for i in temp:
        i[0] = users[i[0]]
        answer.append(i[0]+i[1])
    
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))

'''
먼저 users딕셔너리에 id-nickname 값을 Enter와 Change일 때 넣는다.
temp라는 배열을 만들고 배열의 원소로는 [id, 명령어에 따른 문자열]을
넣는다. temp를 반복문을 돌려 id를 nickname으로 알맞게 바꿔주고
answer에 nickname+문자열을 합한 것을 넣어준다.
'''