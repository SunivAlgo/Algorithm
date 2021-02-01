def solution(clothes):
    answer = 0
    h = {}
    for i in clothes:
        if i[1] in h:
            h[i[1]] += 1
        else:
            h[i[1]] = 1

    for i in h:
        answer *= h[i] + 1
        answer += h[i]

    return answer

'''
처음에는 모든 조합을 구하여 조합끼리의 곱을 answer에 더하는 형싱으로 하였는데 시간초과가 발생했다.

우선은 딕셔너리에 의상종류에 따라 몇개가 있는지 값을 저장하였다. 
그 후  이 문제를 해결 하기 위해 특정 값들을 넣어보면서 규칙성을 찾아보았다. 
규칙은 (의상 수 + 1)을 더해주고 의상 수 만큼 한번더 더해주니 정답이 나왔다.
'''



'''
2 = 2
2 1 = 5
2 1 1 = 11
2 1 1 1 = 23
 
2 2 = 8
2 2 1 = 17
2 2 2 = 26 
2 2 3 = 35 
'''

'''from itertools import combinations

def solution(clothes):
    answer = 0
    h = {}
    for i in clothes:
        if i[1] in h:
            h[i[1]] += 1
        else:
            h[i[1]] = 1
    arr = []
    for i in h:
        answer += h[i]
        arr.append(h[i])

    for i in range(2, len(arr)+1):
        c = list(combinations(arr, i))
        for j in c:
            num = 1
            for k in j:
                num *= k
            answer += num

    return answer'''

clothes = [["a", "a"], ["aa", "a"], ["b", "b"], ["c","c"],["d","s"]]
print(solution(clothes))