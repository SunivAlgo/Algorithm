def find_combi(str1):
    lst=[]
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            lst.append(str1[i:i+2].lower())
    return lst

def find_inter(lst1, lst2):
    cnt = 0
    for x in lst1:
        if x in lst2:   #교집합 원소일 때
            idx = lst2.index(x)
            cnt+=1
            lst2[idx]= ""
    return cnt

def solution(str1, str2):
    lst1 = find_combi(str1)
    lst2 = find_combi(str2)
    if len(lst1)==0 and len(lst2)==0: answer = 1
    else:
        inter_cnt = find_inter(lst1,lst2)
        union_cnt = len(lst1)+len(lst2)-inter_cnt
        answer = inter_cnt/union_cnt

    return int(65536*answer)

# https://blog.naver.com/leemyo_/222265870129