import copy

def rotation(key, M):   # 90도 변경함수
    temp = [[0 for _ in range (M)] for _ in range (M)]
    for i in range(M):
        for j in range(M):
            temp[i][j] = key[M-j-1][i]
    
    return temp

def solution(key, lock):
    M = len(key)
    N = len(lock)
    check = [[0 for _ in range (N + 2*(M-1))] for _ in range (N + 2*(M-1))]     # N + 2*(M-1) 크기로 정사각형 리스트를 만든다.
    for i in range(N):      #가운데에 lock의 모양을 그려 넣는다.
        for j in range(N):
            if lock[i][j] == 1:
                check[i+M-1][j+M-1] = 1

                
    for _ in range(4):      # 90도 변경에 따라 4번 반복해야 한다.
        for i in range(N+M-1):      # check의 크기보다 key의 리스트 크기만큼 작은 부분까지 반복한다.
            for j in range(N+M-1):
                temp = copy.deepcopy(check)     # check 리스트는 만들어 진 것을 계속 써야하기 때문에 복사

                for k in range(M):      #키의 값을 temp에 넣어본다
                    for l in range(M):
                        temp[i+k][j+l] += key[k][l]

                flag = True
                for k in range(N):
                    for l in range(N):
                        if temp[k+M-1][l+M-1] != 1:     #temp 테이블에 lock 부분을 검사하고 다 1이면 true 반환
                            flag = False
                            break
                    if not flag:
                        break
                else:
                    return True
                
        key = rotation(key, M)

    return False

#key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
key = [ [1,1], [0, 1]]
#lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
lock = [[1, 1, 1, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 1, 1]]

print(solution(key, lock))

