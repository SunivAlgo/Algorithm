from itertools import combinations
def solution(orders,course):
    menu = {}
    olen = len(orders)
    for cn in course:
        for od in orders:
            for cb in combinations(od,cn):
                cb = "".join(sorted(list(cb)))
                if cn not in menu:
                    menu[cn] = {}
                    if cb not in menu[cn]:
                        menu[cn][cb] = 1
                else:
                    if cb not in menu[cn]:
                        menu[cn][cb] = 1
                    else:
                        menu[cn][cb] +=1
    ans = []
    for cn in course:
        if cn not in menu:
            continue
        menu_ = sorted(menu[cn].items(),key=lambda x:-x[1])
        max_ = menu_[0][1]
        for m in menu_:
            if max_ != m[1]:
                break
            if m[1] > 1:
                ans.append(m[0])
    return sorted(ans)
            


print(solution(["ABCFG","AC","CDE","ACDE","BCFG","ACDEH"],[2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))