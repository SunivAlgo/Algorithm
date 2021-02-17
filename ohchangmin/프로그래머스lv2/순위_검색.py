
def solution(info, query):
    answer = []
    applicant = []
    for i in info:
        d = {}
        info_split = i.split(' ')
        d['language'] = info_split[0]
        d['occupation'] = info_split[1]
        d['career'] = info_split[2]
        d['soulfood'] = info_split[3]
        d['score'] = int(info_split[4])
        applicant.append(d)
    applicant = sorted(applicant, key=(lambda x: x['score']), reverse=True)
    for i in applicant:
        print(i)
    for i in query:
        info_split = i.split(' and ')
        last_info = info_split[3].split(' ')
        info_split.pop()
        info_split.append(last_info[0])
        info_split.append(int(last_info[1]))
        a = 0
        for j in applicant:
            if info_split[4] > j['score']:
                break
            if (info_split[0] == '-' or info_split[0] == j['language']) and \
            (info_split[1] == '-' or info_split[1] == j['occupation']) and \
            (info_split[2] == '-' or info_split[2] == j['career']) and \
            (info_split[3] == '-' or info_split[3] == j['soulfood']) and \
            (info_split[4] <= j['score']):
                a +=1
        answer.append(a)
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))