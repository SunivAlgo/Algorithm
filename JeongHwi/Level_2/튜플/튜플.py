

import re
def solution(s):
    s_split = s[1:-1]
    s_set = []
    sub_ans = []
    flag = False
    num = ""
    for c in s_split:
        if c == "{":
            continue
        elif c == "}":
            if num != "":
                sub_ans.append(int(num))
                num = ""
            s_set.append(sub_ans)
            sub_ans = []
        elif c == ",":
            if num != "":
                sub_ans.append(int(num))
                num = ""
        else:
            num+=c
    s_set.sort(key=lambda x:len(x))
    ans = []
    for x in s_set:
        for sub in x:
            if sub in ans:
                continue
            ans.append(sub)
    return ans

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))

