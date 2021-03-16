def solution(dirs):
    answer, st_x, st_y = 0, 0, 0
    c = {"U":(1,0), "D":(-1,0), "L":(0,-1), "R":(0,1)}
    road = []

    for loc in dirs:
        new_x, new_y = st_x + c[loc][0], st_y + c[loc][1]
        if -5 > new_x or new_x > 5 or -5 > new_y or new_y > 5: continue

        st, ed = str(st_x)+str(st_y), str(new_x)+str(new_y)
        if st+ed in road or ed+st in road:
            st_x, st_y = new_x, new_y
            continue

        road.append(st+ed)
        st_x, st_y = new_x, new_y
        answer+=1
    
    return answer

# https://blog.naver.com/leemyo_/222277903797