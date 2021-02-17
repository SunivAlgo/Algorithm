from collections import deque
def solution(n):
    nlist = deque([x for x in range(1,n+1)])
    q = deque()
    sums = 0
    ans = 0
    while nlist:
        if sums > n:
            popValue = q.popleft()
            sums -= popValue
        elif sums < n:
            popValue = nlist.popleft()
            sums += popValue
            q.append(popValue)
        elif sums == n:
            ans+=1
            if nlist:
                popValue = nlist.popleft()
                q.append(popValue)
                sums+=popValue
    return ans+1
print(solution(15))


# 다른사람 풀이
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])
# tlqkf
