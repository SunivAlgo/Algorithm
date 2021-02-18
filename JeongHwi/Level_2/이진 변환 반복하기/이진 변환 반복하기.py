def solution(s):
    loop = 0
    count = 0
    while True:
        if s == "1":
            break
        count += s.count("0")
        s = bin(len(s.replace("0","")))[2:]
        loop+=1
    return [loop,count]

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))