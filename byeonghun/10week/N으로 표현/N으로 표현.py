def solution(N, number):
    case_set = [0,[N]]
    if N == number:
        return 1
    for i in range(2, 9):
        temp = []
        s = str(N) * i   
        temp.append(int(s))
        for j in range(1, i//2 + 1):
            for x in case_set[j]:
                for y in case_set[i - j]:
                    temp.append(x * y)
                    temp.append(x - y)
                    temp.append(y - x)
                    temp.append(x + y)
                    if y != 0:
                        temp.append(x // y)
                    if x != 0:
                        temp.append(y // x)
        if number in temp:
            return i
        case_set.append(temp)
    return -1

print(solution(5, 31168))