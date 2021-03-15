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
    
    # print(unique)
    # 최소성 (답을 봄)
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1,len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
                # print(unique[i],unique[j])
    return len(answer)

# ### leemyo_ 풀이
# from itertools import combinations as cb

# def isKey(key, relation):
#     key_lst=[]
#     for i in relation:
#         keyname = ""
#         for j in key:keyname+=i[int(j)]
#         if keyname not in key_lst:
#             key_lst.append(keyname)
#         else:
#             return False      
#     return True     #후보키면 True

# def chkKey(key,e_list):
#     for i in e_list:    #i는 후보키인 애들이다.
#         cnt = 0
#         for j in key:
#             if j in i: cnt+=1
#         if cnt==len(i): return False
#     return True     #없던 후보키 후보이면 True

# def solution(relation):
#     e_list, combi = [], []
#     for i in range(1, len(relation[0])+1):
#         combi += map(''.join,cb([str(i) for i in range(len(relation[0]))], i))
#     print(combi)
#     print("e_list,",e_list) # 키 유일성 확인
#     for i in combi:
#         if chkKey(i,e_list)==False:
#             continue        # 최소성 chk
#         if isKey(i, relation):
#             e_list.append(i)

#     return len(e_list)

# 지혁 풀이
# from itertools import combinations
# def solution(relation):
#     answer = 0
#     row = [i for i in range(len(relation))]
#     column = [i for i in range(len(relation[0]))]
#     key_list = []

#     for i in range(len(column) + 1):
#         if i == 0:
#             continue

#         key_possible_list = list(combinations(column,i)) ## 후보키의 후보들을 추림
#         if key_list: ## 후보들이 있으면
#             print("KeyList,",key_list)
#             save_remove = []
#             for key in key_list:
#                 for check_key in key_possible_list:
#                     if set(key) < set(check_key):
#                         save_remove.append(check_key)

#             for tu in save_remove:
#                 if tu in key_possible_list:
#                     key_possible_list.remove(tu)
#             print("save_remove,",save_remove)
#             print("keyPossible,",key_possible_list)
#             print("=============")
            


#         for key in key_possible_list: ## 후보들을 돌림
#             temp = []
#             for j in row:
#                 temp_list = [relation[j][index] for index in list(key)]
#                 if not temp :
#                     temp.append(temp_list)
#                     continue
#                 if temp_list in temp:
#                     break
#                 temp.append(temp_list)
#             else:
#                 key_list.append(key)

#     answer = len(key_list)

#     return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
