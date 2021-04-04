def solution(a):
    if len(a) == 1:
        return 1
    if len(a) == 2:
        return 2
    answer = 2
    minrlist = sorted(a[2:],reverse=True)
    minr = minrlist.pop()
    minl = a[0]
    for i in range(1, len(a) - 1):
        if a[i] < minr or a[i] < minl:
            answer += 1
        if a[i] < minl:
            minl = a[i]
        if a[i + 1] <= minr:
            while minr <= minrlist[-1]:
                minrlist.pop()
            minr = minrlist.pop()

    return answer


print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))