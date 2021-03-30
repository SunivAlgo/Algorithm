
from copy import deepcopy
min_count = 50
'''
**********find 함수 설명*********
3. 
words 순회하면서 err_count를 검사. err_count -> 글자수가 몇개 다른지 체크

A )     err_count > 1 이면 begin과 글자가 2개 이상 다른 word 이기때문에 break 하고 다음 word 확인

B )     err_count == 1 이면 begin과 글자가 1개 다르다는 뜻이기 때문에 변환 후 더 테스트 해볼 가치가 있음

근데 바뀌는 대상이 target값이면 그때까지의 count가 변환횟수가 된다.
ex) begin = lot, word = log, target = log ::::  lot이 log와 비교될 때 err_count == 1이면서 동시에 log == target이기 때문에 min_count와 비교

바뀌는 대상이 target 값이 아니면 더 테스트 해보기 위해서 begin = word로 바꾼 후, words 리스트에서 word를 삭제(이미 한번 소모했기 때문)
ex) begin = lot, word = log, target = dog :::: lot이 log와 비교 될 때 err_count == 1이면서 begin = word('log')로 설정, log는 words리스트에서 제외 한채로
다음 연산 진행

4.
min_count(초기값=50), count값중 작은값으로 계속 설정
'''



def find(begin, target, words, count):
    global min_count
    print('begin=',begin,'\ntarget=', target, '\nwords=', words, '\n현재 변환횟수=',count,'\n')
    for word in words:
        err_count = 0
        for i in range(len(begin)):
            if begin[i] != word[i]:
                err_count += 1
            if err_count > 1 :
                break
        
        if err_count == 1:
            if word == target:
                min_count = min(min_count,count + 1)
                print('min_count=',min_count,begin,word,target,'\n')
                break

            copy_words = deepcopy(words)
            copy_words.remove(word)
            
            find(word, target, copy_words, count + 1)


def solution(begin, target, words):
    answer = 0 ## answer
    count = 0 ## count = 단어 변환 횟수

    if target not in words: ## 1. words 안에 target이 있는지 확인. 없으면 return 0
        return answer
    find(begin, target, words, count) ## 2. words 안에 target이 있으면 find 함수 진입
    answer = min_count ##answer 값 설정
    return answer

print(solution('hit','cog',["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution('hit','cog',["hot", "dot", "dog", "lot", "log"]))
