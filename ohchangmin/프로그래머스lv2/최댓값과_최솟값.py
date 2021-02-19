def solution(s):
    s = sorted(list(map(int,s.split(' ')))) 
    return str(s[0]) +" "+str(s[len(s)-1]) 

s = "1 2 3 4"
print(solution(s))