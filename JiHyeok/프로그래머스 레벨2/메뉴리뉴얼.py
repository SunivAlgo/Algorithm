from itertools import combinations, permutations
def solution(orders, course):
    answer = []
    

    for i in range(0,len(orders)):
        s = sorted(list(orders[i]))
        orders[i] = ''.join(s)    
    
    for i in course:
        alphabet = set()

        for j in orders:
            if len(j) >= i:
                li = list(combinations(list(j),i))
                for k in li:
                    alphabet.add(''.join(sorted(list(k))))
        
        if not alphabet:
            continue

        alphabet = sorted(list(alphabet))
        li_count = [0]*( len(alphabet) )

        for j in orders:
            if len(j) < i:
                continue
            for k in range(0,len(alphabet)):
                for l in range(0,len(alphabet[k])):
                    if alphabet[k][l] not in j:
                        break
                else: li_count[k] += 1
        
        m = max(li_count)
        for j in range(0,len(li_count)):
            if li_count[j] >= m and li_count[j] >= 2:
                answer.append(alphabet[j])

    answer.sort()
        

    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))

'''
    1.  orders와 course 가 주어짐.
        course에 있는 숫자들 ex)2,3,4 이면
        2 일때
        orders에 들어있는 문자열들 중에 제일 많이 나오는 길이 = 2 인 문자열을 찾아야 한다.

    2.  그러기 위해서는 문자열의 길이가 2 이상일 때, 그 문자열 안에서 조합가능한 문자열들을 찾아준다.
        ex) ABCFG -> A,B  A,C  A,F  A,G  B,C ........ F,G 까지.
        이것을 alphabet 집합에 넣어주었음.
        orders의 나머지 문자열들에게도 똑같은 방법을 적용하여 alphabet 집합에 가능한 조합들을 넣는다.

    3.  alphabet 집합을 리스트로 바꾸고, alphabet 크기만큼의 count_list를 생성하여, alphabet 안의 문자열들이
        orders의 문자열들 안에 있으면 해당하는 count_list의 index를 +1.
        ex ) ABCFG -> 1  1  1  1  1  ......
                      AB AC AF AG BC ......
             AC    -> 1  2  1  1  1  ......
                      AB AC AF AG BC ......
    4.  count_list의 max값에 해당하는 index를 alphabet에 적용하면 제일 많이 쓴 문자열 조합이 나온다.
'''