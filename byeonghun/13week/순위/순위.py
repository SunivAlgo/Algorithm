from collections import defaultdict

def solution(n, results):
    answer = 0
    d = {}
    rank = {}
    for r in results:
        if r[0] not in d:
            d[r[0]] = [[r[1]],[]]
        else:
            d[r[0]][0].append(r[1])
        if r[1] not in d:
            d[r[1]] = [[],[r[0]]]
        else:
            d[r[1]][1].append(r[0])
    return d

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))