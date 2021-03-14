def solution(dirs):
    now_y = now_x = 0
    route = set()
    d = {"U":[1,0],"D":[-1,0],"R":[0,1],"L":[0,-1]}
    for op in dirs:
        dy = d[op][0]
        dx = d[op][1]
        if not(-5<=now_y+dy<=5 and -5<=now_x+dx<=5):
            continue
        
        # Before
        bef_y = now_y
        bef_x = now_x
        # After
        now_y += dy
        now_x += dx

        route.add((now_y,now_x,bef_y,bef_x))
        route.add((bef_y,bef_x,now_y,now_x))
    return len(route)//2

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
print(solution("LRLRL"))