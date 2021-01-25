def solution(a, b):
    answer = ''    
    count = 0
    for i in range(1,a):
        if i==1:
            count +=31
        elif i==2:
            count+=29
        elif i==3:
            count+=31
        elif i==4:
            count+=30
        elif i==5:
            count+=31
        elif i==6:
            count+=30
        elif i==7:
            count+=31
        elif i==8:
            count+=31
        elif i==9:
            count+=30
        elif i==10:
            count+=31
        elif i==11:
            count+=30
        elif i==12:
            count+=31
    
    count +=b

    if count%7==0:
        answer = 'THU'
    elif count%7==1:
        answer = 'FRI'
    elif count%7==2:
        answer = 'SAT'
    elif count%7==3:
        answer = 'SUN'
    elif count%7==4:
        answer = 'MON'
    elif count%7==5:
        answer = 'TUE'
    elif count%7==6:
        answer = 'WED'
    return answer