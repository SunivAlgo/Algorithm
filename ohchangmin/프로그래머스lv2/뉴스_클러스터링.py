import math

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    d1 = {}
    for i in range(0, len(str1)-1):
        if str1[i:i+2].isalpha():
            if str1[i:i+2] in d1:
                d1[str1[i:i+2]] += 1
            else:
                d1[str1[i:i+2]] = 1
    
    gyo = 0
    hap = 0

    for i in range(0, len(str2)-1):
        if str2[i:i+2].isalpha():
            if str2[i:i+2] in d1 and d1[str2[i:i+2]] != 0:
                d1[str2[i:i+2]] -= 1
                gyo += 1
            hap += 1

    if len(d1) == 0 and hap == 0:
        return 65536

    for i in d1:
        if d1[i] > 0:
            hap += d1[i]
    
    return math.floor(gyo/hap * 65536)


str1 = "aa1+aa2"
str2 = "AAAA12"

print(solution(str1, str2))



'''
가장 처음 str1의 요소들을 뽑아내어 딕셔너리에 저장한다.
중복될경우 value를 1씩 증가시켜 숫자만큼 저장한다.
str2의 요소들을 뽑으면서 딕셔너리에 해당 값이 0이 아닌채로 존재하는지
살펴보고 있을 경우 교집합의 변수를 1증가 후 딕셔너리 값을 1 뺀다.
합집합의 변수는 계속 1씩 증가한다.
반복문을 마치고 서로 공집합일 경우를 체크한다. if len(d1) == 0 and hap == 0:
그 이후 딕셔너리에 남아있는 value의 숫자들을 합집합 변수에 더하며
교집합, 합집합의 수를 구한다.

isalpha() 알아둘 것
'''