def solution(a):
    answer = 0
    l_min,r_min=[0 for i in range(len(a))],[0 for i in range(len(a))]
    
    m = a[0]
    for i in range(len(a)):
        if m>a[i]: m = a[i]
        l_min[i] = m
    m = a[len(a)-1]
    for i in range(len(a)-1,-1,-1):
        if m>a[i]: m = a[i]
        r_min[i] = m
        
    for i in range(len(a)):
        if a[i]<=l_min[i] or a[i]<=r_min[i]: answer+=1
    
    return answer    

#