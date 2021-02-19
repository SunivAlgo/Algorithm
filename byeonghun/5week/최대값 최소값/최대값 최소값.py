def solution(s):
    slist = list(map(int, s.split()))
    print(slist)
    return str(min(slist)) + ' ' + str(max(slist))

print(solution("1 2 3 4"))