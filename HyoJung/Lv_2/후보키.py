from itertools import combinations as cb

def isKey(key, relation):
    key_lst=[]
    for i in relation:
        keyname = ""
        for j in key:keyname+=i[int(j)]
        if keyname not in key_lst:
            key_lst.append(keyname)
        else:
            return False      
    return True     #후보키면 True

def chkKey(key,e_list):
    for i in e_list:    #i는 후보키인 애들이다.
        cnt = 0
        for j in key:
            if j in i: cnt+=1
        if cnt==len(i): return False
    return True     #없던 후보키 후보이면 True

def solution(relation):
    e_list, combi = [], []
    for i in range(1, len(relation[0])+1):
        combi += map(''.join,cb([str(i) for i in range(len(relation[0]))], i))
    
    for i in combi:
        if chkKey(i,e_list)==False:
            continue        # 최소성 chk
        if isKey(i, relation):
            e_list.append(i)

    return len(e_list)

# https://blog.naver.com/leemyo_/222272087638