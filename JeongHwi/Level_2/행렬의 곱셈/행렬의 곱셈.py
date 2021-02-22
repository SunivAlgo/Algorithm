def product(x,y):
    sums = 0
    for k in zip(x,y):
        sub = 1
        for i in k:
            sub*=i
        sums+=sub
    return sums

def solution(arr1,arr2):
    arr2_ = []
    for i in range(len(arr2[0])):
        sub=[]
        for j in range(len(arr2)):
            sub.append(arr2[j][i])
        arr2_.append(sub)
    ans = []
    for x in arr1:
        sub = []
        for y in arr2_:
            sub.append(product(x,y))
        ans.append(sub)
    return ans

print(solution([[1, 4], [3, 2], [4, 1]],[[3,3],[3,3]]))