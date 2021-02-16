def solution(s):
    arr=list(s.split())
    arr=[int(i) for i in arr]
    arr.sort()
    return str(arr[0])+" "+str(arr[-1])

#https://blog.naver.com/leemyo_/222244673695