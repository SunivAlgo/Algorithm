
def solution(numbers, hand):
    
    answer = ''
    righthand = 10
    lefthand = 12
    rightdistance = 0
    leftdistance = 0



    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            lefthand = i
            answer += 'L'
        elif i == 3 or i == 6 or i== 9:
            righthand = i
            answer += 'R'
        else :
            if i == 0:
                i += 11
            rightdistance = int(abs(righthand - i) / 3) + (abs(righthand - i) % 3)
            leftdistance = int(abs(lefthand - i) / 3) + (abs(lefthand - i) % 3)
            if rightdistance < leftdistance:
                righthand = i
                answer +='R'
            elif leftdistance < rightdistance:
                lefthand = i
                answer += 'L'
            else:
                if hand == "right":
                    righthand = i
                    answer += 'R'
                else :
                    lefthand = i
                    answer += 'L'
    return answer