def solution(s):
    s = list(s)
    for i in range(len(s)):
        if i == 0:
            if s[i] == " ":
                continue
            if "a"<=s[i]<="z":
                s[i] = s[i].upper()
                continue
        if s[i-1] == " ":
            if "a"<=s[i]<="z":
                s[i] = s[i].upper()
        else:
            if "A"<=s[i]<="Z":
                s[i] = s[i].lower()
    return "".join(s)
print(solution("3people unFollowed me"))
print(solution(" i don't            know          asd"))
print(solution("for the last  WeEk"))
print(solution("         a        a         b         c    "))