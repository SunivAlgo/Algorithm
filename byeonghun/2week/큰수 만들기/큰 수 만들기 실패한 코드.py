def solution(number, k):
    nlist = list(number)
    maxi = 0
    for i in range(0, k + 1):
        if nlist[maxi] < nlist[i]:
            maxi = i
    del nlist[0:maxi]
    k -= maxi
    if k == 0:
        return ''.join(nlist)
    for j in range(k):
        for i in range(len(nlist)):
            if i == len(nlist) - 1:
                nlist.pop(i)
                break
            if nlist[i] < nlist[i + 1]:
                nlist.pop(i)
                break
    return ''.join(nlist)

print(solution("1231234", 3))