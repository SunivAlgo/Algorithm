def sol(li,n):
    ans = []
    t = []
    for i in  li:
        temp = i
        while(temp!=0):
          t.append(temp % 2)
          temp = int(temp / 2)
        while len(t) < n:
            t.append(0)
        t.reverse()
        ans.append(t)
        t = [] 
    return ans
def solution(n, arr1, arr2):

    answer = []
    a1=[[]]
    a2=[[]]

    t = []
    p = []

    a1 = sol(arr1,n)
    a2 = sol(arr2,n)

    for i in range(0,len(a1)):
        for j in range(0,len(a1[i])):
            p.append(a1[i][j] + a2[i][j])
        t.append(p)
        p = []

    a = ""

    for i in range(0,len(t)):
        for j in range(0,len(t[i])):
            if t[i][j] >= 1:
                a += "#"
            else:
                a += " "
        answer.append(a)
        a = ""
    return answer


'''
    1. 받은 배열 두개의 원소들을 2진법으로 표현하여 2차원배열로 만듦
    2. 두 2차원 배열 +
    3. 0이 아닌부분을 #으로 0인부분은 " "으로 다른 2차원 배열 생성
'''