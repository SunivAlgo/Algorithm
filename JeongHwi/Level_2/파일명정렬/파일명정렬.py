from collections import deque
def compiles(file):
    head = ""
    number = ""
    i =0
    filelen = len(file)
    # HEAD Split
    while True:
        if i<filelen:
            # print(head)
            if not file[i].isdigit():
                head += file[i]
                i+=1
            else:
                break
    # NUMBER Split
    for j in range(i,filelen):
        if file[j].isdigit():
            number+=file[j]
            continue
        break
    # print((head,number))
    return head,number

def solution(files):
    ans = []
    for file in files:
        head,number = compiles(file)
        ans.append((head.lower(),int(number),file))
    ans.sort(key=lambda x:(x[0],x[1]))
    return [x[2] for x in ans]

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
print(solution(["img000012345", "img1.png","img2","IMG02"]))

