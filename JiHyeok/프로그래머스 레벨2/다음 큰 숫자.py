import time
def calculate (b):
    answer = 0
    count = 1
    for i in range(len(b)-1,-1,-1) :
        answer += count * b[i]
        count *= 2
    return answer

def sol(b):
    if 0 not in b:
        b[1] = 0
        b.append(1)
        return calculate(b)
    else:
        idx = b.index(0)
        if 1 not in b[idx:]:
            b.append(0)
            b = b[:1] + list(reversed(b[1:]))
            return calculate(b)
        else :
            end = 0
            changeIdx = 0
            for i in range(len(b)-1,-1,-1):
                if b[i] == 1:
                   end = i
                   break
            for i in range(end,-1,-1):
                if b[i] == 0:
                    changeIdx = i
                    break
            temp = b[changeIdx]
            b[changeIdx] = b[changeIdx + 1]
            b[changeIdx + 1] = temp
            b = b[:changeIdx + 1] + [0] * b[changeIdx + 1:].count(0) + [1] * b[changeIdx + 1:].count(1)
            return calculate(b)
    return answer

def binary(n):
    b = []
    while(n > 0):
        b.append(n % 2)
        n = n // 2
    return list(reversed(b))

def solution(n):
    start = time.time()
    answer = 0
    b = binary(n)
    answer = sol(b)
    end = time.time()
    print(end-start)
    return answer
print(solution(999999))
'''
    1.  n의 2진수 리스트 b 구하기
    
    2.  만약 b 에 0이 없으면 ex) 1,1,1,1,1
        자리수 늘리고 b[1] = 0 하여 바로 answer return
    
    3.  (ㄱ) 0이 있으면
        (ㄴ) 0의 index -> Idx 라 하면 b[Idx:] 에서 1 이 있는지 확인
        
            ex) 1,1,1,0,0,0 or 1,1,1,1,0 or 1,1,0,0,0,0 같은 부류를 찾기 위함
            없으면 위와 같은 것들이므로 b.append(0) 하고
            answer = b[0:1] + reversed(b[1:])
    
    4.  (ㄴ) 0의 index -> Idx 라 하면 b[Idx:] 에서 1 이 있는지 확인
            ex) 1,1,1,0,0,1,1,0   or    1,1,1,0,0,1,1,0,1
            있으면 위와같은 것들임

        (ㄷ) b의 뒤에서부터 1을 찾기 시작 (e)
            ex) 1,1,1,0,0,1,1,0   or    1,1,1,0,0,1,1,0,1
                            e                           e
        
        (ㄹ) e부터 앞으로 오면서 0을 찾기 시작 (c)
            ex) 1,1,1,0,0,1,1,0   or    1,1,1,0,0,1,1,0,1
                      i c   e                 i       c e

        (ㅁ) b[c]와 b[c+1]을 바꾸고
             b = b[:c+1] +   { b[c+1:] 중에서 0,1의 개수를 파악하여 0*0의 개수, 1*1의 개수 만큼 추가해준 리스트}
    
'''