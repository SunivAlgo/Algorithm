def solution(msg):
    answer = []
    d = {}
    for i in range(26):     #우선 A~Z 까지 1 ~26 으로 사전에 저장
        d[chr(ord('A')+i)] = i+1
    
    add_num = 27
    i = 0
    while i < len(msg):
        s = ""
        for j in range(i, len(msg)):
            s += msg[j]
            if not s in d:  #문자열에 문자를 계속 더하여 그 문자열 이 사전에 없을 때까지 확인
                answer.append(d[s[:-1]])    #문자열에서 마지막 문자 제거 후 정답에 추가
                d[s] = add_num  # 사전 숫자 지정
                add_num += 1
                i = j   # msg에서 다음에 시작할 인덱스 지정
                break
        else:   # 마지막 조건 시 answer에 추가 ex) kakao 에서 o
            answer.append(d[s])
            break
            
    return answer

msg = "TOBEORNOTTOBEORTOBEORNOT"
print(solution(msg))