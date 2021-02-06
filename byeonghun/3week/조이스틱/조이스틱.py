def findi(fixed, i):
    right = 1
    left = 1
    k = i + 1
    while k < len(fixed) and fixed[k] == True:
        right += 1
        k += 1
    j = (i - 1 + len(fixed)) % len(fixed)
    while fixed[j] == True:
        left += 1
        j = (j - 1 + len(fixed)) % len(fixed)

    if left >= right :
        return k , right
    else:
        return j , left

def solution(name):
    answer = 0
    alist = ['A' for i in range(len(name))]
    fixed = [False for i in range(len(name))]
    for i in range(len(name)):
        if name[i] == 'A':
            fixed[i] = True
    i = 0
    while True:
        temp = 0
        if ord(name[i]) > 78:
            temp = abs(ord(name[i]) - 91)
        else:
            temp = ord(name[i]) - ord(alist[i])
        alist[i] = name[i]
        fixed[i] = True
        if sum(fixed) == len(name):
            answer += temp
            break
        i , v = findi(fixed, i)
        answer += temp + v
    return answer

print(solution("jAAAAAA"))