
def solution(files):
    answer = []
    number_list = ['0','1','2','3','4','5','6','7','8','9']

    for i in range(len(files)):
        s = files[i]
        index = 0
        head = ''
        number = ''
        tail = ''
        while s[index] not in number_list :
            head += s[index]
            index += 1

        while index < len(s) and s[index] in number_list:
            number += s[index]
            index += 1

        while index < len(s):
            tail += s[index]
            index += 1

        files[i] = [head,number,tail]
    
    files.sort( key = lambda file : (file[0].upper() , int(file[1])) )

    answer = [''.join(file) for file in files]

    return answer
print(solution(["img12", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
'''
    1.  head, number, tail을 담은 리스트를 files에 저장
    
    2.  file[0] (head) 를 upper한것을 비교하여 사전순 정렬

    3.  두번째기준은 file[1] (number)를 int 한것을 비교하여 정렬
'''