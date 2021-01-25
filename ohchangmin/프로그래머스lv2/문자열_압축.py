def solution(s):
    answer = 1000
    temp = []
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s)//2 + 1):
        for j in range(0, len(s), i):
            temp.append(s[j:j+i])

        compression = ""
        num = 1
        for j in range(0, len(temp)):
            if j == len(temp)-1 or temp[j] != temp[j+1]:
                if num != 1:
                    compression += str(num)
                compression += temp[j]
                num = 1
            else:
                num += 1
        if answer > len(compression):
            answer = len(compression)
        temp.clear()
    
    return answer

s = "xababcdcdababcdcd"
print(solution(s))

'''
s의 길이가 1이면 1을 반환.
그외에는 s를 1부터 s의 절반 까지의 단위로 나눠서 temp에 저장하는 것을 반복한다.
temp가 리스트의 형식으로 나눠진 문자열들을 저장하고 있기 때문에 문제에서 원하는
압축 문자열을 만들기가 쉽다. (인덱스마다 연속되어 있다면 카운트를 통해 숫자 + 문자열 형식을 만들어 줌)
''' 