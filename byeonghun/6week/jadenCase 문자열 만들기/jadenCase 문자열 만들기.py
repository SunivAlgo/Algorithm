def solution(s):
    s = s.lower()
    slist = s.split(" ")
    for i in range(len(slist)):
        slist[i] = slist[i].capitalize()

    return ' '.join(slist)