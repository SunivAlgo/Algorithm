def solution(dirs):
    now = [0,0]
    d = {}

    for i in dirs:
        forward = now.copy()    # 나아갈 방향
        if i == 'U':    #조건문에 따라 좌표 + 1
            forward[0] += 1 
        elif i == 'D':
            forward[0] -= 1
        elif i == 'R':
            forward[1] += 1
        elif i == 'L':
            forward[1] -= 1
        if forward[0] < -5 or forward[0] > 5 or forward[1] < -5 or forward[1] > 5:      # 좌표판 넘어갈 시
            continue
        key = [now[0], now[1], forward[0], forward[1]]      # 진행방향, 그 반대방향도 저장해야 그 길 자체를 지난것에 대해 판단이 가능하다 (딕셔너리에 경로 추가)
        key = ','.join(list(map(str, key)))
        d[key] = 1
        key = [forward[0], forward[1], now[0], now[1]]
        key = ','.join(list(map(str, key)))
        d[key] = 1

        now = forward.copy()    #현재 위치를 업데이트 한다
     
    return len(d) // 2      #한 길을 지날때 마다 2개씩 추가했으므로 2로 나눈다.


dirs = "ULURRDLLU"	
print(solution(dirs))