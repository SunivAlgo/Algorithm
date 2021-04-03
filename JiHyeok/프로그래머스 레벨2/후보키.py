from itertools import combinations
def solution(relation):
    answer = 0
    row = [i for i in range(len(relation))]
    column = [i for i in range(len(relation[0]))]
    key_list = []
    
    for i in range(len(column) + 1):
        if i == 0:
            continue

        key_possible_list = list(combinations(column,i)) ## 후보키의 후보들을 추림
        if key_list: ## 후보들이 있으면
            save_remove = []
            for key in key_list:
                for check_key in key_possible_list:
                    if set(key) < set(check_key):
                        save_remove.append(check_key)

            for tu in save_remove:
                if tu in key_possible_list:
                    key_possible_list.remove(tu)

        
        for key in key_possible_list: ## 후보들을 돌림
            temp = []
            for j in row:
                temp_list = [relation[j][index] for index in list(key)]
                if not temp :
                    temp.append(temp_list)
                    continue
                if temp_list in temp:
                    break
                temp.append(temp_list)
            else:
                key_list.append(key)
    answer = len(key_list)
    
    return answer


print(solution( [['a', 'aa'], ['aa', 'a'], ['a', 'a']]))
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
'''
    1.  combinations 으로 후보키의 후보들을 만든다. ex) (1,0) (2,0) (3,0) .....(0,1,2,3)....

    2.  후보키에 본래 들어있었으면 후보키리스트에서 제외
        ex) (1,) 이 후보키(answer) 안에 있으면 1이 들어가는 튜플들(1,0),(1,2),(1,3),(1,4) 등등은 모두 지움

    3.  그렇게 남겨진 것들 중에서 후보키를 추린다.
'''