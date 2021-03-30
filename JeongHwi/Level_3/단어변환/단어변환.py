# DFS Height 구하는 문제?...인가?
from pprint import pprint
from collections import deque

def search(begin,target,words,alphaSet):
    q = deque()
    visit = {word:0 for word in words}
    visit[begin] = 1
    q.append(begin)
    while q:
        nowNode = q.popleft()
        if nowNode == target:
            # print(visit)
            return visit[nowNode]-1
        for i,now in enumerate(nowNode):
            for ch in alphaSet[i]:
                if ch == now:
                    continue
                newWord = nowNode[:i]+ch+nowNode[i+1:]
                if newWord in words and not visit[newWord]:
                    visit[newWord] = visit[nowNode]+1
                    q.append(newWord)
    return 0
def solution(begin,target,words):
    # init
    alphaSet ={i:set() for i,_ in enumerate(begin)}
    for word in words:
        for i,w in enumerate(word):
            alphaSet[i].add(w)
    pprint(alphaSet)
    return search(begin,target,words,alphaSet)
        



print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"]), 1)
print(solution("1234567000", "1234567899", ["1234567800", "1234567890", "1234567899"]), 3)
print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"]), 4)