arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]

def check(y,x,step,arr):
    for i in range(y,y+step):
        for j in range(x,x+step):
            if arr[i][j] != arr[y][x]:
                return False
    return True
def quardZip(y,x,arr,step,ans):
    if check(y,x,step,arr):
        ans[arr[y][x]]+=1
        return
    step//=2
    for i in range(2):
        for j in range(2):
            quardZip(y+i*step,x+j*step,arr,step,ans)

def solution(arr):
    x = y = len(arr)
    num = y
    ans = {0:0,1:0}
    quardZip(0,0,arr,num,ans)
    return [ans[0],ans[1]]

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))