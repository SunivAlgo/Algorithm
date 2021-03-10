def solution(n, t, m, p): ## n : 진법, t : 미리구할 숫자의 개수, m : 참가인원, p : 튜브의 순서
    answer = ''
    number_list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    count = 1 ## 순서를 가르쳐주는 수
    number_game = 0 ## 게임을 진행하는데 필요한 수
    
    ## 순서계산시 %가 0이 나올때가 있음. 따라서 m==p 이면 p를 ㅎ그냥 0으로 바꿨다.
        ## ex ) 참가인원 2명에 2번째순서일때
    
    if m == p:
        p = 0
    def calculate_number_li(number_game): ## 10진수 숫자를 n진수로 바꿔서 list형태로 반환
        li = []
        if number_game == 0:
            return ['0']
        
        
        while number_game != 0: 
            li.append(number_list[number_game % n])
            number_game //= n
        
        return li

    while(True):
        cal_li = calculate_number_li(number_game) ## n진수로 바꾼 리스트를 넘겨받음
        

        '''
            1. cal_li 가 존재하고, answer의 길이가 t보다 작은동안 반복
            2. 루프마다 pop. 순서를 나타내는 count가 조건에 맞을때마다 튜브의 답을 저장
        '''

        while cal_li and len(answer) < t: ## 1.
            number = cal_li.pop() ## 2.
            if count % m == p: ## 2.
                answer += number
            count += 1

        if len(answer) >= t: ## answer의 길이가 t이면 멈춤.
            break
        number_game += 1
    return answer

print(solution(2,4,2,1))
print(solution(16,16,2,1))
print(solution(16,16,2,2))
'''
    1.  
'''

