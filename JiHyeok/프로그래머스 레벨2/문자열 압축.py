def solution(s):
    answer = 0
    index = 0
    leastnumber = 0
    number = 0
    
    for i in range(1,len(s)+1):
        compare = s[0:i]
        count = 0
        
        while index + i <= len(s):
            if s[index:index + i] == compare:
                count += 1
                index += i
            else :
                number += i
                if count != 1:
                    number += len(str(count))
                compare = s[index:index+i]
                count = 0
        number += i
        if count != 1:
            number += len(str(count))

        if index < len(s):
            number += len(s) - index
        
        

        if leastnumber == 0:
            leastnumber = number
        else:
            if leastnumber > number:
                leastnumber = number
        
        
        number = 0
        index = 0
        


    answer = leastnumber
    return answer
print(solution("xababcdcdababcdcd"))