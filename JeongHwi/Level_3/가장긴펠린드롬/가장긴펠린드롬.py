def solution(s):
    # 펠린드롬은 1도 있음
    """
    효율성 안따지고 구현
    """
    maxAns = -1
    slen = len(s)
    for i in range(slen):
        for j in range(i+1,slen):
            target = s[i:j+1]
            rTarget = target[::-1]
            if target == rTarget:
                # print(target, rTarget)
                maxAns = max(maxAns, j-i+1)
                # print(maxAns)
    if maxAns == -1:
        return 1
    return maxAns
print(solution("abcdcba"),7)
print(solution("abacde"),3)
