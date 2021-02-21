import sys
sys.setrecursionlimit(20000)

def zero_or_one(arr, x, y, w, h):
    temp = 0
    for i in range(y, h):
        for j in range(x , w):
            temp += arr[i][j]
    if temp == 0:
        return 0
    elif temp == (w - x) * (h - y):
        return temp
    else :
        return -1

def divide(arr, x, y ,w, h):
    _0 = 0
    _1 = 0
    wm = (w + x) // 2
    hm = (h + y) // 2
    lu = zero_or_one(arr, x, y, wm, hm)
    ru = zero_or_one(arr, wm, y, w, hm)
    ld = zero_or_one(arr, x, hm, wm, h)
    rd = zero_or_one(arr, wm, hm, w, h)
    if lu == 0: _0 += 1
    elif lu > 0: _1 += 1
    else : 
        temp = divide(arr, x, y, wm, hm)
        _0 += temp[0]
        _1 += temp[1]
    if ru == 0: _0 += 1
    elif ru > 0: _1 += 1
    else :
        temp = divide(arr, wm, y, w, hm)
        _0 += temp[0]
        _1 += temp[1]
    if ld == 0: _0 += 1
    elif ld > 0: _1 += 1
    else :
        temp = divide(arr, x, hm, wm, h)
        _0 += temp[0]
        _1 += temp[1]
    if rd == 0: _0 += 1
    elif rd > 0: _1 += 1
    else :
        temp = divide(arr, wm, hm, w, h)
        _0 += temp[0]
        _1 += temp[1]   
    return [_0, _1]

def solution(arr):
    temp = zero_or_one(arr, 0, 0, len(arr), len(arr))
    if temp > 0:
        return [0, 1]
    elif temp == 0:
        return [1, 0]
    else:
        return divide(arr, 0, 0, len(arr), len(arr))

print(solution([[1,1],[1,1]]))

# print(solution([
#     [1,1,1,1,1,1,1,1],
#     [0,1,1,1,1,1,1,1],
#     [0,0,0,0,1,1,1,1],
#     [0,1,0,0,1,1,1,1],
#     [0,0,0,0,0,0,1,1],
#     [0,0,0,0,0,0,0,1],
#     [0,0,0,0,1,0,0,1],
#     [0,0,0,0,1,1,1,1]]))
