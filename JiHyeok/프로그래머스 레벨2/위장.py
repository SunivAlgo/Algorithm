
def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        if i[1] in dic:
            dic[i[1]] = dic[i[1]] + 1
        else :
            dic[i[1]] = 1
    
    for i in dic.keys():
        answer *= dic[i] + 1

    return answer - 1

print(solution([['a','aa'],['b','bb'],['c','cc'],['d','dd']]))


'''
    1.  2차 배열의 마지막 원소가 category 이므로 clothes를 1차 리스트로 만들었음

    2.  각 category를 count로 세어 리스트로 저장했음

    3.  count 를 순회하면서 곱해주는데, 안입는 것을 생각해서 각 원소마다 +1 시켜줘서 곱,
        마지막 answer에는 모두 안입을 경우를 생각해서 -1       ---------------> 이 방법이 생각 안났음

    4.  그런데 두 문제가 틀려서 생각해 봤더니 이런 반례를 생각해 냄

        [head, head], [head, head] , [head,head] 가 있으면 내 방법에선 head를 6번을 찾게 됨.
        따라서 구조를 dictionary 형태로 바꿔줬다.
'''