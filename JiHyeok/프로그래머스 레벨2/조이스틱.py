from collections import deque

def calculate(now_index,Qnumber,length):
    number = abs(now_index - Qnumber)
    if number > length//2:
        number = length - number
    return number

def leftright(dQ,name):
    now_index = 0
    count = 0
    while dQ:
        left = calculate(now_index,dQ[0],len(name))
        right = calculate(now_index,dQ[-1],len(name))
        if left > right:
            now_index = dQ.pop()
            count += right
            count += updown(name[now_index])

        else:
            now_index = dQ.popleft()
            count += left
            count += updown(name[now_index])
    return count

def updown(s):
    if ord(s) <= ord('N'):
        count = ord(s) - ord('A')
    else:
        count = 26 - (ord(s) - ord('A'))
    return count

def solution(name):
    li = []
    for i in range(0,len(name)):
        if name[i] != 'A':
            li.append(i)
    dQ = deque(li)
    
    answer = leftright(dQ,name)

    return answer
    
print(solution('AABAAAAAAABBB'))

'''
    소모시간 2시간 30분...
    
    알고리즘을 푸는 것에 두가지 계산이 있습니다.
    a.  왼쪽 오른쪽으로 인덱스를 옮기는 계산
    b.  위 아래 알파벳 철자를 바꾸는 계산

    1.  위 아래 알파벳 철자를 바꾸는 계산은 쉽습니다.
        a.  A에서 얼마만큼 떨어져 있는지 확인하여 up 할지 down할지 판별해야 한다.
        b.  위의 updown 함수를 쉽게 풀어쓰면
            s <= N 이면 count = s - A
            s > N이면 count = 26 - s - 'A'
    
    2.  index를 설정하는 방법
        a.  'A'이지 않은 원소들을 모은 리스트를 추린다.
        b.  리스트[0] 과 리스트[-1]을 index_now 와 비교하여 어느쪽이 더 가까운지 계산.
        c.   더 작은쪽과 index_now와의 거리를 구하고, 그것을 pop하는 동시에 index_now 갱신        
'''