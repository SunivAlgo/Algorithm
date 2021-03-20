def solution(dirs):
    answer = 0
    ud = [[False for _ in (range(11))] for _ in range(10)]
    lr = [[False for _ in (range(10))] for _ in range(11)]
    x = 5
    y = 5
    for i in dirs:
        if i == 'U' and y > 0:
            y -= 1
            if ud[y][x] == False:
                answer += 1
                ud[y][x] = True
        elif i == 'D' and y < 10:
            y += 1
            if ud[y - 1][x] == False:
                answer += 1
                ud[y - 1][x] = True
        elif i == 'L' and x > 0:
            x -= 1
            if lr[y][x] == False:
                answer += 1
                lr[y][x] = True
        elif i == 'R' and x < 10:
            x += 1
            if lr[y][x - 1] == False:
                answer += 1
                lr[y][x - 1] = True

    return answer

print(solution("ULURRDLLU"))