def solution(routes):
    routes.sort(key = lambda x:x[1])
    cm_loc, ans = routes[0][1], 1
    
    for i in routes:
        if i[0]<= cm_loc:
            continue
        ans+=1
        cm_loc = i[1]
    return ans

# https://blog.naver.com/leemyo_/222297150067