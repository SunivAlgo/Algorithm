def solution(n, t, m, p):
    answer = ''
    d = {}
    for i in range(0, 17):   # 0~16 까지 숫자에 따른 문자를 저장 ex) 1='1', A='10'
        if i <= 9:
            d[i] = str(i)
        else:
            d[i] = chr(ord('A') + (i%10))
    
    decimal_num = 0  # 10진수 형태로 계속 증가 하는 숫자
    turn = 1
    while len(answer) < t:
        chaneg_num = ""
        if decimal_num == 0:    #처음 시작일때는 chaneg_num를 ""이 아닌 0을 채워줘야함
            chaneg_num = "0"

        temp_num = decimal_num
        while temp_num > 0:     # chaneg_num에 decimal_num을 적당한 진수로 바꾼 값을 넣어줌
            chaneg_num = d[temp_num % n] + chaneg_num
            temp_num //= n 

        while chaneg_num:   # 만들어진 chaneg_num을 한문자씩 쪼개어 연산하는 반복문
            if turn == p:   # 내 차례 때 해당 문자를 answer에 더해줌
                answer += chaneg_num[0]
                if len(answer) == t:    # 전체 코드 종료시점 
                    break
            chaneg_num = chaneg_num[1:] # chaneg_num은 앞이 하나씩 잘림
            turn += 1
            if turn > m:    # 내 차례가 m을 넘어가면 차례를 1로 초기화
                turn = 1
        
        decimal_num += 1

    return answer

n = 16
t = 16
m = 2
p = 2
print(solution(n, t, m, p))