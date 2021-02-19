def solution(name):
    answer = 0
    num = []
    for i in name:
        n = ord(i) - ord('A')
        if n <= 13:
            num.append(n)
        else:
            num.append(26 - n)
    print(num)

    zs = ze = 0
    ts = te = 0
    noZero = True
    flag = False
    for i in range(0, len(num)):

        if num[i] == 0 and not flag:
            noZero = False
            ts = te = i
            flag = True
        elif num[i] == 0 and flag :
            te = i
        if num[i] != 0 or i == len(num)-1:
            if ze - zs <= te - ts:
                zs = ts
                ze = te
            flag = False
    if noZero:
        zdist = 0
    else:
        zdist = ze - zs + 1
    rdist = zs - 1
    ldist = len(num)-1 - ze 
    print(zs, ze)
    print("zdist = ",zdist, " rdist = ",rdist, " ldist = ",ldist)
    if zdist == 0 or (zdist < rdist and zdist < ldist):
        answer = sum(num)
        answer += len(num) -1
    elif rdist < ldist and rdist >= 0:
        for i in range(0, zs):
            answer += num[i]
        answer += 2*rdist
        for i in range(ze+1, len(num)):
            answer += num[i]
        answer += ldist
    else:
        for i in range(0, zs):
            answer += num[i]
        answer += rdist
        for i in range(ze+1, len(num)):
            answer += num[i]
        answer += 2*ldist
    return answer

#AAABAAAAB
name = "AABAAAAA"
print(solution(name))