def solution(s):
    answer = ''
    count = 0
    for i in range(0,len(s)):
        if s[i] == " ":
            count = 0
            answer += " "
            continue
        if count % 2 == 0: # 짝수일때
            answer += s[i].upper()
            count += 1
        else: # 홀수일때
            answer += s[i].lower()
            count += 1
    
    return answer