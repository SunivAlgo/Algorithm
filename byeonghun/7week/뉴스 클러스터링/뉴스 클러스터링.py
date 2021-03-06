def todict(s):
    strdict = dict()
    for i in range(0, len(s)-1):
        if s[i].isalpha() and s[i+1].isalpha():
            substr = s[i:i+2]
            if substr in strdict:
                strdict[substr] += 1
            else:
                strdict[substr] = 1
    return strdict

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    dict1 = todict(str1)
    dict2 = todict(str2)
    if len(dict1) == 0 and len(dict2) == 0:
        return 65536
    uni = 0
    inter = 0
    for i in dict1.keys():
        if i in dict2:
            inter += dict1[i] if dict1[i] < dict2[i] else dict2[i]

    uni = sum(dict1.values()) + sum(dict2.values()) - inter

    return int((inter/uni) * 65536)

print(solution("aa1+aa2", "AAAA12"))