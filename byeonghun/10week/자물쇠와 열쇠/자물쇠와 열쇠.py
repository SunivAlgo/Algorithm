def rotate(key):
    lenk = len(key)
    rkey = [[0] * lenk for _ in range(lenk)]
    for r in range(lenk):
        for c in range(lenk):
            rkey[c][lenk-1-r] = key[r][c]
    return rkey
def check(key, lock, s, e, i, j, sumlock):
    correct = 0
    for x in range(i, i + len(key)):
        for y in range(j, j + len(key)):
            if x < s or y < s or x >= e or y >= e: continue
            if lock[x - s][y - s] + key[x - i][y - j] != 1:
                return False
            if lock[x - s][y - s] == 0 and  key[x - i][y - j] == 1:
                correct += 1
    if sumlock + correct == len(lock) * len(lock):
        return True
    else:
        return False
def solution(key, lock):
    s = len(key) - 1
    e = s + len(lock)
    sumlock = 0
    for i in lock:
        for j in i:
            sumlock += j
    for _ in range(4):
        for i in range(e):
            for j in range(e):
                if check(key, lock, s, e, i, j, sumlock):
                    return True
        key = rotate(key)
    return False

print(solution([
    [0, 0, 0], 
    [1, 0, 0], 
    [0, 1, 1]],[ 
    [1, 1, 1], 
    [1, 1, 0], 
    [1, 0, 1]]))