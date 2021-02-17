def solution(s):
    answer = ""
    s = sorted(list(map(int,s.split(' '))))
    answer = str(s[0]) +" "+str(s[len(s)-1])  
    return answer

s = "1 2 3 4"
print(solution(s))