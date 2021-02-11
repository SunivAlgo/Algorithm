from itertools import combinations

def solution(orders, course):
    answer = []
    for i in course:
        temp = {}
        for order in orders:
            if len(order) < i: continue
            for j in combinations(order, i):
                listj = list(j)
                listj.sort()
                coursename = "".join(listj)
                if coursename in temp:
                    temp[coursename] += 1
                else:
                    temp[coursename] = 1
        if not temp: continue
        most = max(temp.values())
        if most <= 1: continue
        for key in temp.keys():
            if temp[key] == most:
                answer.append(key)
    answer.sort()
    return answer


print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))