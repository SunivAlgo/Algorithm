from itertools import combinations
from bisect import bisect_left
def solution(info, queries):
    answer = []
    dic = dict()
    
    for i in range(len(info)):
        info[i] = info[i].split()
        for j in range(5):
            li_com = list(combinations(info[i][:-1],j))
            for k in li_com:
                s = ''.join(list(k))
                if s in dic.keys():
                    dic[s].append(int(info[i][-1]))
                else:
                    dic[s] = [int(info[i][-1])]
    
    for i in dic.keys():
        dic[i].sort()

    for i in range(len(queries)):
        queries[i] = queries[i].split()
        for n in range (3):
            queries[i].remove('and')
        while '-' in queries[i]:
            queries[i].remove('-')
        s = ''.join(queries[i][:-1])
        if s in dic.keys():
            idx = bisect_left(dic[s],int(queries[i][-1]))
            count = len(dic[s]) - idx ### 효율성에서 중요!!!!
            answer.append(count)
            continue
        answer.append(0)
        
    return answer
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

'''
    1.  info 에 있는 문자열들을 파싱하여 딕셔너리에 들어갈 key들을 만들어주고
        그 key의 value는 점수를 넣은 list이다.

        ex ) java backend junior pizza 150
             -> java , 150
             -> backend , 150
             -> junior , 150
             -> pizza , 150
             -> javabackend, 150
             -> .....
             -> backendjuniorpizza , 150
             -> javabackendjuniorpizza , 150
             각 info마다 총 16개의 key가 만들어짐

    2.  각 key의 value들을 점수에 따라서 sort 해준다

    3.  query에 들어있는 문자열을 파싱하여 해당 key의 value에 접근, 점수 이상인 원소들의 개수를 구한다.
        여기서 bisect라는 파이썬 내 이진탐색 라이브러리를 활용하였다.

        ex ) query = 'java and - and junior and - and 80'
             -> javajunior , 80 을 구할 수 있다
             -> javajunior로 딕셔너리를 검색하여 80이상인 원소들을 세어주면 된다.

    *** 계속 시간초과가 되어 어떤것이 문제인지 고민하던중, 제시점수 이상의 원소들을 세어주는 과정에서
        리스트를 슬라이스한 길이를 구하는 것이 문제였음
        ex) len(li[0:-1])이라고 표현하면 'li[0:-1]를 슬라이스 한 것'의 길이를 구하는것 이므로 시간이 굉장히 오래 걸린다
        
'''