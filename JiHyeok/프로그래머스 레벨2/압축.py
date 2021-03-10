
from collections import deque
def solution(msg):
    answer = []
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dictionary = {}
    index_dictionary = 1
    ### dictionary 초기화
    for s in alphabet:
        dictionary[s] = index_dictionary
        index_dictionary += 1

    msg = deque(msg)
    
    while msg:
        s = msg[0] ## s = msg의 첫문자
        index_find = 0 ## dictionary 에서 s로 찾은 값. 일단 0으로 초기화
        '''
        ex) 'KOKOBOL'
            1. s = 'K' , s 는 dictionary 안에 있으므로 루프 진입
            2. msg의 첫 원소 'K'는 dictionary안에 있는 key이므로 leftpop
            3. index_find 에는 dictionary[k] = 11 이므로 11 저장
            4. leftpop을 했는데 msg에 아무것도 없을 시 다음 루프를 못돌기때문에 break
            5. s += msg[0] ---> s = 'KO'인 채로 다음루프를 돎
        '''
        while s in dictionary: ## 1
            msg.popleft() ## 2
            index_find = dictionary[s] ## 3
            if len(msg) == 0: ## 4
                break
            s += msg[0] ## 5
        '''
            6. s = 'KO' 인상태 이므로 dictionary에 등록
            7. index_dictionary ++
            8. answer에 11 추가
        '''
        dictionary[s] = index_dictionary ## 6.
        index_dictionary += 1 ## 7.
        answer.append(index_find) ## 8.

    
    return answer

print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print(solution('ABABABABABABABAB'))