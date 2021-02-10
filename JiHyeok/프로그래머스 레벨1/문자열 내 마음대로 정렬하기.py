def solution(strings, n):
    answer = []
    alphabet = []
    temp = []
    for i in range (0,ord('z')-ord('a') + 1):
        alphabet.append(chr(i + ord('a')))

    for i in alphabet:
        for j in strings:
            if j[n] == i:
                temp.append(j)
        if temp:
            temp.sort()
            for k in temp:
                answer.append(k)
        temp = []
    return answer


    
'''
    1. a ~ z 까지 담긴 alphabet 리스트 구현
    2. alphabet 리스트와 strings 를 비교하며 같은게 있으면 temp 리스트에 넣음
    3. temp 리스트를 사전순으로 정렬
    4. answer에 순서대로 넣는다.
'''