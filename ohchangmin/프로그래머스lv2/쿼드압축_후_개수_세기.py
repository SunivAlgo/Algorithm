answer = [0, 0]

def DC(arr):
    if len(arr) == 1:
        if arr[0][0] == 0:
            answer[0] += 1
        else:
            answer[1] += 1
        return
    sarr = sum(arr, [])
    if sum(sarr) == 0:
        answer[0]+=1
        return
    elif len(sarr) == sum(sarr):
        answer[1]+=1
        return
    A = []
    a1=[]
    a2=[]
    a3=[]
    a4=[]
    for i in range(0, len(arr)//2):
        a = []
        for j in range(0, len(arr)//2):
            a.append(arr[i][j])
        a1.append(a)
    for i in range(len(arr)//2, len(arr)):
        a = []
        for j in range(0, len(arr)//2):
            a.append(arr[i][j])
        a2.append(a)
    for i in range(0, len(arr)//2):
        a = []
        for j in range(len(arr)//2, len(arr)):
            a.append(arr[i][j])
        a3.append(a)
    for i in range(len(arr)//2, len(arr)):
        a = []
        for j in range(len(arr)//2, len(arr)):
            a.append(arr[i][j])
        a4.append(a)
    A.append(a1)
    A.append(a2)
    A.append(a3)
    A.append(a4)

    for i in A:
        sa = sum(i, [])
        if sum(sa) == 0:
            answer[0]+=1
        elif len(sa) == sum(sa):
            answer[1]+=1
        else:
            DC(i)

def solution(arr):
    DC(arr)
    return answer

arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
print(solution(arr))


'''
재귀를 반복한다.
들어온 2차원 배열을 4등분으로 나누어 4개의 리스트에 각각 기록한 후 리스가 전부 0이나 1인지
확인하고 answer값을 더해준다. 정사각형 안에 다른 값이 있을 경우는 해당 정사각형을 재귀함수 인자로
넣어 위와같은 방법을 재개한다. 1개일 경우는 해당 데이터(0 or 1)을 answer에 더해준다.
'''