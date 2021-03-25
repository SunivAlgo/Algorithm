import copy
def getRotate(keys,m): # Rotate 90 Degree.
    result = [[0 for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            result[j][m-i-1] = keys[i][j]
    return result

def check(n,m,pad,key,i,j,lockS):
    temp = copy.deepcopy(pad)
    for y in range(m):
        for x in range(m):
            temp[y+i][x+j] = temp[y+i][x+j]^key[y][x]
    
    
    for y in range(m-1,m-1+n):
        for x in range(m-1,m-1+n):
            if temp[y][x] == 0:
                return False
    return True

def adj_Padding(lock,n,keys,m):
    # m+n-2, Padding
    pad = [[0 for _ in range(n+m*2-2)] for _ in range(n+m*2-2)]
    for i in range(m-1,n+m-1):
        for j in range(m-1,n+m-1):
            pad[i][j] = lock[i-m+1][j-m+1]
    
    lockS = m-1
    for k in keys:
        for i in range(n+m-1):
            for j in range(n+m-1):
                if check(n,m,pad,k,i,j,lockS):
                    return True
    return False
                    


def solution(key,lock):
    m = len(key)
    n = len(lock)
    
    ro_90_key = getRotate(key,m)
    ro_180_key = getRotate(ro_90_key,m)
    ro_270_key = getRotate(ro_180_key,m)

    keys = [key,ro_90_key,ro_180_key,ro_270_key]
    return adj_Padding(lock,n,keys,m)
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))