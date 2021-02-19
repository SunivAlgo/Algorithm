def solution(s):
    answer = [0,0]
    while s != "1":
        prevL = len(s)
        s = s.replace("0",'')
        nowL = len(s)
        answer[1] += (prevL - nowL)
        s = bin(nowL)[2:]
        answer[0] += 1
  
    return answer

s = "110010101001"
print(solution(s))

'''
적절히 문제대로 작성하면 가능
replace, bin 사용
'''