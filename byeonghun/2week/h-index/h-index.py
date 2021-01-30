def solution(citations):
    cnt = 0
    citations.sort(reverse= True)
    for i in range(len(citations)):
        if i + 1 != len(citations):
            if citations[i] <= cnt and citations[i + 1] <= cnt:
                break
        else:
            if citations[i] <= cnt:
                break
        cnt += 1
    return cnt

print(solution([10, 10, 10, 10]))