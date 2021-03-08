from collections import Counter
import re
def makeSub(strs):
    strs = strs.lower()
    subList = []
    for i in range(len(strs)-1):
        subString = strs[i]+strs[i+1]
        if re.match("[a-z][a-z]",subString):
            subList.append(subString)
    return subList

def solution(str1,str2):
    str1List = makeSub(str1)
    # print(str1List)
    str2List = makeSub(str2)
    # print(str2List)
    ins = 0
    uni = 0
    count1 = Counter(str1List)
    count2 = Counter(str2List)

    uniSet = set(str1List).union(str2List)
    insSet = set(str1List).intersection(str2List)
    for i in insSet:
        ins += min(count1[i],count2[i])
    # print(ins)
    for u in uniSet:
        uni += max(count1[u],count2[u])
    # print(uni)
    if uni == 0:
        return 65536
    return int((ins/uni)*65536)

print(solution("FRANCE","FRENCH"))
print(solution("handshake","shake hands"))
print(solution("aa1+aa2","AAAA12"))
print(solution("E=M*C^2","e=m*c^2"))