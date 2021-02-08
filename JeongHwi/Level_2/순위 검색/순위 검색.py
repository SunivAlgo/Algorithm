from itertools import combinations
from bisect import bisect_left
infos = {}
def getinfos(score,info_):
    global infos
    for k in range(5):    
        for x in combinations([0,1,2,3],k):
            case = ""
            for i in range(4):
                if i not in x:
                    case += info_[i]
                else:
                    case += "-"
            if case not in infos:
                infos[case]=[int(score)]
            else:
                infos[case].append(int(score))

def solution(info,query):
    for i in info:
        info_split = i.split()
        score = info_split[-1]
        info_ = info_split[:-1]
        getinfos(score,info_)
    for x in infos.keys():
        infos[x].sort()
    ans = []
    for q in query:
        q = q.replace("and","")
        q_split = q.split()
        condition = "".join(q_split[:4])
        score = int(q_split[4])
        if condition in infos:
            ans.append(len(infos[condition])-bisect_left(infos[condition],score,lo=0,hi=len(infos[condition])))
        else:
            ans.append(0)
    return ans

# 시간초과 코드
"""
from collections import Counter
def condition_Check(conditions,applicants):
    sub_ans = []
    notCondition = 0
    for i,cond in enumerate(["language","job","career","soulFood"]):
        if conditions[i] == "-":
            for x in applicants[cond]:
                sub_ans += applicants[cond][x]
            continue
        sub_ans += applicants[cond][conditions[i]]
    counter = [x for x,c in Counter(sub_ans).items() if c == 4]
    # print(counter)
    count = 0
    for i in counter:
        if int(applicants["score"][i]) >= int(conditions[4]):
            count+=1
    return count
def solution(info,query):
    # init
    applicants = {"language":{"java":[],"cpp":[],"python":[]},
                  "job":{"backend":[],"frontend":[]},
                  "career":{"junior":[],"senior":[]},
                  "soulFood":{"chicken":[],"pizza":[]},
                  "score":{}}
    for number,info_ in enumerate(info):
        infos = info_.split()
        applicants["language"][infos[0]].append(number)
        applicants["job"][infos[1]].append(number)
        applicants["career"][infos[2]].append(number)
        applicants["soulFood"][infos[3]].append(number)
        applicants["score"][number] = infos[4]
    # pprint.pprint(applicants)
    ans = []
    # query
    for q in query:
        query_Split = q.split()
        conditions = [query_Split[0],query_Split[2],query_Split[4],query_Split[6],query_Split[7]]    
        ans.append(condition_Check(conditions,applicants))
    return ans
"""