# IN
# [닉네임]이 들어왔습니다.
# OUT
# [닉네임]이 나갔습니다.
# CHANGE
# OUT -> Change -> IN, 기존 채팅방에 있는 아이디도 변경

from collections import deque
def solution(record):
    database = {}
    opQueue = deque()
    for r in record:
        data = r.split()
        if data[0] == "Enter":
            database[data[1]] = data[2]
            opQueue.append([data[0],data[1]])
        elif data[0] == "Leave":
            opQueue.append([data[0],data[1]])
        elif data[0] == "Change":
            database[data[1]] = data[2]
    ans = []
    while opQueue:
        operation,id = opQueue.popleft()
        if operation == "Enter":
            ans.append(database[id]+"님이 들어왔습니다.")
        elif operation == "Leave":
            ans.append(database[id]+"님이 나갔습니다.")
    return ans
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))