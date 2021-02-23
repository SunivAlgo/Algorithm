
def solution(s):
    answer = ''
    switch = 1
    for i in s:
        if i == ' ':
            answer += i
            switch = 1
            continue
        elif switch == 1:
            answer += i.upper()
            switch = 0
            continue
       
        answer += i.lower()
    return answer
print(solution("    p e o   3p l e unF oLlowed me  "))
'''
    처음에는 공백을 기준으로 문자열을 split하여 각 원소의 첫글자만 upper 나머지는 lower
    해주면 끝이라고 생각.

    공백이 여러개일 수도 있었다. 따라서 단어의 첫글자인지 아닌지 판별하는
    switch 변수를 두었음.
    1 == 지금의 문자가 대문자가 되어야 한다.
    0 == 지금의 문자가 소문자가 되어야 한다.
    초기 switch = 1
    
    i = 문자열 순회 변수

    1.  제일 먼저 확인해야 하는 조건은
        i == ' '(공백)
        
        TRUE면 answer에 추가
        switch = 1로 변경

    2.  그 다음 조건은
        switch == 1

        TRUE면 answer에 대문자로 추가
        switch = 0 으로 변경

    3.  조건에 걸러지지 않은 것들은
        모두 소문자로 변경.
        

'''