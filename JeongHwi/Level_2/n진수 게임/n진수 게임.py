"""
n : 진법 수
t : 미리 구할 숫자의 개수
m : 참가하는 인원
p : 튜브의 순서
"""

info_16 = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}

def getBase_N(n,i):
    convert_n = []
    if i == 0:
        return [0]
    while i != 0:
        r = i%n
        m = i//n
        # print("r:",r,"m:",m)
        i=m
        if r > 9:
            r = info_16[r]
        convert_n.append(str(r))
    return reversed(convert_n)

def solution(n,t,m,p):
    ans = []
    i=0
    now = 0 # 사람 순서를 의미
    count = 0
    while t >= count:
        # print("count",len(count),t)
        cn = getBase_N(n,i)
        for c in cn:
            # print((now%m)+1,c)
            if (now%m)+1 == p: #튜브 차례!
                # print("Tube Turn!")
                ans.append(str(c))
                count+=1
                if count == t:
                    break
            now+=1
        i+=1
    return "".join(ans[:t])
print(solution(2,4,2,1))
print(solution(16,16,2,1))
print(solution(16,16,2,2))