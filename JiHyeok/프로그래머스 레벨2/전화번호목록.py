
from collections import deque
def solution(phone_book):
    answer = True
    phone_book.sort()
    dQ = deque(phone_book)
    while dQ:
        for i in range(1,len(dQ)):
            if dQ[i].find(dQ[0]) != -1:
                answer = False
                return answer
            if dQ[0][0] != dQ[i][0]:
                break
        dQ.popleft()
    return answer

print(solution(["119","97674223", "1195524421"]	))

'''
    <내가 푼방법>
    1.  phone_book 리스트를 복사한 deque를 만든다.
    2.  deque[0] 이 deque[1] ~ deque[-1]까지 돌면서
        a.  만약 접두에 붙으면 답이 나왔으므로 answer = False를 return
        b.  deque[0][0] 이 deque[n][0]과 다르다면 이제 접두일 일이 없으므로 break
    3.  아무일도 일어나지 않았다면 popleft.




    정렬을 하고 startswitch를 쓰면 더 깨끗하게 풀 수 있음.
    s.startswitch(n,0) s가 0에서 시작하는지 알 수 있음.
    s.endswitch(n,0,6) s가 5에서 끝나는지 알 수 있음.

    또 for문에서 zip 함수를 썼으면 더 깨끗하게 할 수 있음
    ex) for p1, p2 in zip(dQ,dQ[1:]):
'''