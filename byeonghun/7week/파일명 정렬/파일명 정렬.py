import re

def solution(files):
    temp = [re.split(r"([0-9]+)", i) for i in files]
    answer = sorted(temp, key = lambda x:(x[0].lower(), int(x[1])))
    return ["".join(s) for s in answer] 

print(solution(	["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))