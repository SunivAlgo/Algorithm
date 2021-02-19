def solution(s):
    temp = []
    answer = []
    ob = {}
    slist = s.split(',')
    for i in slist:
        i = i.replace('{', '').replace('}', '')
        num = int(i)
        if num in ob:
            ob[num] += 1
        else:
            ob[num] = 1
    for i in ob:
        temp.append([ob.get(i), i])
    temp.sort(reverse = True)
    for i in temp:
        answer.append(i[1]) 
    return answer


print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))