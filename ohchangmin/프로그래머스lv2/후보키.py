from collections import deque
from itertools import combinations
# 못품
def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])  

    candidates=[]
    for i in range(1,n_col+1):  # 모든 조합의 경우의 수를 index로 저장
        candidates.extend(combinations(range(n_col),i))

    final=[]
    for keys in candidates:
        tmp=[tuple([item[key] for key in keys]) for item in relation]   #각각 경우에 수에 따른 key값들을 얻어옴
        if len(set(tmp))==n_row: # 중복되는 것이 없다면 파이널에 해당 인덱스 조합을 추가
            final.append(keys)
    
    answer=set(final[:])    #discard를 하기 위해 set으로 복사 
    for i in range(len(final)):
        for j in range(i+1,len(final)):
            if len(final[i])==len(set(final[i]).intersection(set(final[j]))):   # final[i]가 모두 들어 있는 final[j] 가 있을 경우(insersection 으로 교집합 수를 구하여 알아냄)
                answer.discard(final[j])                                        # answer에서 final[j] 제거 
                
    return len(answer)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))

'''
set.intersection() : 교집합
set.discard() : removed와 기능은 같으나 지우려는 것이 없어도 오류 발생 x

배열안에 똑같은 배열의 원소가 있는지 확인하는 부분을 해결하지 못했고 발견해도 제대로 지우는 부분을 생각하지 못했다.
'''