def level1(new_id):
    new_id=new_id.lower()
    return new_id
def level2(new_id):
    for i in "~!@#$%^&*()=+[{]}:?,<>/":
        new_id = new_id.replace(i,"")
    return new_id
def level3(new_id):
    while new_id.find("..") != -1:
        new_id=new_id.replace("..",".")
    return new_id
def level4(new_id):
    if new_id != "":
        if new_id[0] == ".":
            new_id = new_id[1:]
    if new_id != "":
        if new_id[-1] == ".":
            new_id = new_id[:-1]
    return new_id
def level5(new_id):
    if new_id == "":
        new_id+="a"
    return new_id
def level6(new_id):
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = level4(new_id)
    return new_id
def level7(new_id):
    if len(new_id) <=2 :
        while len(new_id) != 3:
            new_id+=new_id[-1]
    return new_id
def solution(new_id):
    new_id = level1(new_id)
    new_id = level2(new_id)
    new_id = level3(new_id)
    new_id = level4(new_id)
    new_id = level5(new_id)
    new_id = level6(new_id)
    new_id = level7(new_id)
    return new_id

# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
# print(solution("=.="))
# print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))
print(solution("a................b"))