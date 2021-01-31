def solution(brown, yellow):
    answer = []
    rect = brown + yellow
    for i in range(1 , int(rect / 2)):
        if rect % i == 0:
            a = rect / i
            if (a-2) * (i-2) == yellow:
                if a-2 >= i-2:
                    answer.append(a)
                    answer.append(i)
                else:
                    answer.append(i)
                    answer.append(a)
                break
    return answer

print(solution(24, 24))