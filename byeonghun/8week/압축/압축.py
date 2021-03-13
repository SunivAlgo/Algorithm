def solution(msg):
    answer = []
    zip = dict()
    for i in range(1, 27):
        zip[chr(64 + i)] = i
    indx = 27
    i = 0
    while i < len(msg):
        j = 0
        while i + j < len(msg):
            word = msg[i:i + j + 1]
            if word not in zip:
                zip[word] = indx
                indx += 1
                break
            j += 1
        answer.append(zip[msg[i:i+j]])
        i += j
    return answer


print(solution("TOBEORNOTTOBEORTOBEORNOT"))