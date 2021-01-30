from itertools import combinations
from functools import reduce
def solution(clothes):
    answer = 0
    hashing = {}
    for i in clothes:
        if i[1] in hashing:
            hashing[i[1]] += 1
        else:
            hashing[i[1]] = 1
    answer += len(clothes)
    for i in range(2, len(hashing.keys()) + 1):
        clist = list(combinations(hashing.values(),i))
        print(clist)
        for j in clist:
            answer += reduce(lambda x, y : x * y , j)
    return answer

print(solution(	[
["a","aa"],
["a_a","bb"],
["aaa","cc"],
["ccc","cc"],
["ccc","cc"],
["ddd","dd"]
]))