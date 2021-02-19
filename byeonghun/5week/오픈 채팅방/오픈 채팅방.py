def solution(record):
    answer = []
    user = {}
    position = 0
    for i in record:
        word = i.split()
        if word[0] == 'Change':
            user[word[1]][0] = word[2]
            continue
        
        if word[0] == 'Enter':
            answer.append("님이 들어왔습니다.")
            if word[1] in user:
                user[word[1]][0] = word[2]
                user[word[1]][1].append(position)
            else:
                user[word[1]] = [word[2], [position]]
        else:
            answer.append("님이 나갔습니다.")
            user[word[1]][1].append(position)
        
        position += 1
    
    for id in user.values():
        for i in id[1]:
            answer[i] = id[0] + answer[i]
    
    return answer

print(solution(["Enter uid1234 Muzi", 
                "Enter uid4567 Prodo",
                "Leave uid1234",
                "Enter uid1234 Prodo",
                "Change uid4567 Ryan"]))