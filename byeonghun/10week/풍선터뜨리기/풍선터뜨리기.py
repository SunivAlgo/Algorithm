def solution(a):
    if len(a) == 1:
        return 1
    if len(a) == 2:
        return 2
    answer = 2
    maxr = max(a[2:])
    maxl = a[0]
    for i in range(1, len(a) - 1):
        if a[i] == maxr:
            for j in range(i + 1, len(a)):
                if maxr > a[j]:
                    maxr = a[j]
                    break
        if a[i] < maxr or a[i] < maxl:
            answer += 1
        if maxl > a[i]:
            maxl = a[i]
    return answer


print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))