from itertools import combinations, permutations
def solution(orders, course):
    answer = []
    

    for i in range(0,len(orders)):
        s = sorted(list(orders[i]))
        orders[i] = ''.join(s)    
    
    li = set(combinations(list(orders[0]),2))
    for i in li:
        answer.append(''.join(sorted(list(i))))
    print(li)

    return answer
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))