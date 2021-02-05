numbers=[1,1,1,1,1]
target = 3

count=0
def back(numbers,nlen,target,nlist,i,flag): 
    global count
    # print(nlist)
    if i == nlen:
        if sum(nlist) == target:
            count+=1
        return
    nlist.append(numbers[i])
    back(numbers,nlen,target,nlist,i+1,"+")
    nlist.pop()
    nlist.append(-numbers[i])
    back(numbers,nlen,target,nlist,i+1,"-")
    nlist.pop()
def solution(numbers,target):
    nlen = len(numbers)
    back(numbers,nlen,target,[],0,"home")
    return count

print(solution(numbers,target))