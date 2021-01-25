def solution(answers):
    n=[]
    answer = []
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    
    s1count = 0
    s2count = 0
    s3count = 0

    for i in range(0,len(answers)):
        if answers[i]==s1[i%5]:
            s1count+=1
        if answers[i]==s2[i%8]:
            s2count+=1
        if answers[i]==s3[i%10]:
            s3count+=1
    
    n.append(s1count)
    n.append(s2count)
    n.append(s3count)

    m = max(n)
    if n[0]==m:
        answer.append(1)
    if n[1]==m:
        answer.append(2)
    if n[2]==m:
        answer.append(3)

    return answer