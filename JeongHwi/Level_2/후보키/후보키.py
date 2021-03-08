from itertools import combinations
def getSubData(re_dict,keys):
    s = []
    for k in keys:
        s.append(re_dict[k])
    sub = []
    for i in range(len(s[0])):
        sub.append(tuple([x[i] for x in s]))
    return sub
        

def solution(relation):
    relen = len(relation)
    inlen = len(relation[0])
    re_dict = {}
    #initialize Dictionary
    for i in range(inlen):
        re_dict[i] = []
    for r in relation:
        for i in range(inlen):
            re_dict[i].append(r[i])
    
    # Get Unique
    unique = []
    for i in range(1,len(re_dict)+1):
        for x in combinations(re_dict.keys(),i):
            subData = getSubData(re_dict,x)
            if len(set(subData)) == relen:
                unique.append(x)
    # print(unique)
    print(unique)
    # 최소성 (답을 봄)
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1,len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
                print(unique[i],unique[j])
    return len(answer)
        



print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))