def solution(number, k):
    answer = ''
    r_size = len(number) - k
    start = 0
    end = len(number) - r_size+1

    while True:
        m = 0
        for i in range(start, end):
            if int(number[i]) == 9 or m < int(number[i]):
                m = int(number[i])
                start = i+1
                if m == 9:
                    break
        answer += str(m)
        end += 1
        if len(answer) == r_size:
            break

    return answer

number = "4177252841"
k = 4
print(solution(number, k))

'''
number 안에서 최대숫자를 찾는 범위를 계속 설정해주어서 최대숫자들을 합하여
최대값을 만든다. 범위는 예를 들어 최종적으로 만들어야 하는 값의 길이가 5이라면
number의 마지막 4개의 문자를 제외하여 범위를 설정한다. 최대값을 찾게 되면
최대숫자의 다음 인덱스 부터 마지막 3개 문자를 제외한 범위를 지정하여 최대값을 
찾는다. 이를 반복한다. 
문자가 9라면 9는 최대이니 최대숫자를 찾는 것을 멈추고 반복문을 나갈 수 있다.
저 부분을 넣지 않으니 검사시 시간 초과가 난 케이스가 있었다. number가 9를 제외
한 다른 숫자 하나로만 이루어진 긴 문자열이라면 시간초과가 날 것 같다. 그래서 
좋은 코드는 아니라고 생각한다.
'''