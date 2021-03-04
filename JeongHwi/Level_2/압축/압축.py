import string
def solution(msg):
    # Uppercase Dictionary
    dics = dict([(x,i+1) for i,x in enumerate(string.ascii_uppercase)])
    dics_num = 26
    ans = []

    msglen = len(msg)
    target = ""
    for i in range(0,msglen):
        if i == msglen-1: # Last alphabet check
            ans.append(dics[target+msg[i]])
            break

        target+=msg[i]
        if target+msg[i+1] in dics: # word in Dictionary
            # print("in Dict",target)
            continue
        else: # not in Dictionary
            dics_num+=1
            dics[target+msg[i+1]] = dics_num
            ans.append(dics[target])
            target = ""

    
    return ans


print(solution("KAKAO"))
# print(solution("TOBEORNOTTOBEORTOBEORNOT"))
# print(solution("ABABABABABABABAB"))
