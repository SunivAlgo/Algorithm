def make_slice(file):
    idx, lst = 0, ["","",""]
    while file[idx].isnumeric()==False:
        lst[0]+=file[idx]; idx+=1
    
    while file[idx].isnumeric()==True:
        lst[1]+=file[idx]; idx+=1
        if idx==len(file): break

    if len(lst[1])>5:
        lst[1], lst[2] = lst[:5], lst[5:]
    if idx<len(file): lst[2]+=file[idx:]

    return lst

def solution(files):
    answer = []
    
    for x in files: answer.append(make_slice(x))
    answer = sorted(answer, key=lambda x: (x[0].lower(),int(x[1])))
    
    return [''.join(x) for x in answer]

# https://blog.naver.com/leemyo_/222265989139