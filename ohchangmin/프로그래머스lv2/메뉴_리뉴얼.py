from itertools import combinations

def solution(orders, course):
    answer = []
    h = {}
    c = []
    for order in orders:
        add = []
        for i in order:
            add.append(i)
        c.append(add)

    for i in course:
        h[i] = {}
        for j in c:
            sort_j = sorted(j)
            com = list(combinations(sort_j, i))
            for k in com:
                h_add = ""
                for l in k:
                    h_add += l
                length = len(h_add)
                if h_add in h[length]:
                    h[length][h_add] += 1
                else:
                    h[length][h_add] = 1
    
    for i in h:
        max = 0             
        for j in h[i]:
            if max < h[i][j]:
                max = h[i][j]
        if max >= 2:
            for j in h[i]:
                if max == h[i][j] :
                    answer.append(j)

    return sorted(answer)

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course))

'''
가장 먼저 orders의 문자열들을 문자로 나누어 c리스트에 문자열마다 따로 저장을 한다. 
["XYZ", "XWY", "WXA"] -> [['X', 'Y', 'Z'], ['X', 'W', 'Y'], ['W', 'X', 'A']] 

course에 있는 숫자들 만큼 각각에 나눠진 문자열들의 문자를 가지고 조합을 시켜 문자열을 생성한다. 
이 때 combinations을 하기전에 문자들을 순서대로 정렬시킨다. ("XWY", "WXA" 여기서 WX를 공통으로 처리하기 위해)
조합된 문자열을 딕션너리에 추가하고 중복시 값을 증가 시킨다.
딕셔너리는 그 안에 문자열 크기만큼으로 구분되는 또다른 딕셔너리가 있다.

{2: {'XY': 2, 'XZ': 1, 'YZ': 1, 'WX': 2, 'WY': 1, 'AW': 1, 'AX': 1}, 
 3: {'XYZ': 1, 'WXY': 1, 'AWX': 1}, 
 4: {}}
 문자열 크기로 나눠진 딕셔너리 각각에서 최대값을 찾아 최대값과 일치하는 문자열을 answer에 추가시키고 정렬 후 반환한다.
'''