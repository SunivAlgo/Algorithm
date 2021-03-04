def solution(files):
    answer = []
    info = []
    for i in files:
        head = ""
        number = ""
        flag = False
        for j in range(0, len(i)):
            if i[j] >= "0" and i[j] <= "9":
                flag = True
            if flag and not(i[j] >= "0" and i[j] <= "9"):
                break
            if not flag:
                head += i[j]
            else:
                number += i[j]
        info.append([i, head.upper(), int(number)])
    
    info.sort(key=lambda x : (x[1], x[2]))

    for i in info:
        answer.append(i[0])
    return answer
    
files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(solution(files))


'''
files의 각각의 요소들을 [파일이름, 헤더, 숫자] 로 저장하고 해당 리스트들의
이 차원 리스트를 만든다. ex) [[파일이름, 헤더, 숫자], [파일이름, 헤더, 숫자]]
헤더는 대문자, 숫자는 int식으로 바꿔서 저장
이차원 리스트를 람다식에 맞춰서 정렬한 후 파일이름만 따로 추출하여 답을 만든다.
'''