def solution(dartResult):
    numberList = []
    answer = 0
    for i in range (0, len(dartResult)):
        if ord('0') <= ord(dartResult[i]) <= ord('9'):
            if dartResult[i+1] == '0':
                numberList.append(10)
                i += 1
            elif i != 0 and dartResult[i-1] == '1':
                continue
            else:
                numberList.append(int(dartResult[i]))
        elif dartResult[i] == 'S' or dartResult[i] == 'D' or dartResult[i] == 'T':
            if dartResult[i] == 'S':
                numberList[-1] = numberList[-1] ** 1
            elif dartResult[i] == 'D':
                numberList[-1] = numberList[-1] ** 2
            elif dartResult[i] == 'T':
                numberList[-1] = numberList[-1] ** 3
        elif dartResult[i] == '*' or dartResult[i] == '#':
            if dartResult[i] == '*':
                numberList[-1] *= 2
                if len(numberList) >= 2:
                    numberList[-2] *= 2
            elif dartResult[i] == '#':
                numberList[-1] *= -1

    for i in numberList:
        answer += i
    return answer
'''
    1. 문자열 구분은 숫자로
'''