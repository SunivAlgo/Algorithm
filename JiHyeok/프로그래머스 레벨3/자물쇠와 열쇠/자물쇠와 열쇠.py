from copy import deepcopy
def rotation_90(key):
    n = len(key)
    newkey = []
    for x in range(n):
        temp_li = []
        for y in range(n):
            temp_li.append(key[n-1-y][x])
        newkey.append(temp_li)
    return newkey

def solution(key, lock):
    answer = False
    keys = []
    keys.append(key)
    for i in range(3):
        key = deepcopy(rotation_90(key))
        keys.append(key)

    lock_hom = []
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                lock_hom.append([i,j])
    
    keys_hom = []
    for i in range(len(keys)):
        key_hom = []
        for a in range(len(keys[i])):
            for b in range(len(keys[i])):
                if keys[i][a][b] == 1:
                    key_hom.append([a,b])
        keys_hom.append(key_hom)

    for key_hom in keys_hom:
        for li in key_hom:
            
    
    

    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))