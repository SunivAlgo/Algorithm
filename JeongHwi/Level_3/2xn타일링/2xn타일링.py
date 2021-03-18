def solution(n):
    pre2 = 1
    pre1 = 2
    for i in range(3,n+1):
        next_ = pre2+pre1
        pre2,pre1 = pre1,next_
    print(pre2,pre1)
    

print(solution(4))