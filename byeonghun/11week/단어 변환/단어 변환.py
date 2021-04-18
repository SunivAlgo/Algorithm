from collections import deque

def check(a, b):
    answer = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            answer += 1
        if answer > 1:
            return -1 # 완전 불일치
    if answer == 1: # 하나빼고
        return 1
    else: #일치
        return 0 
def solution(begin, target, words):
    if target not in words:
        return 0
    que = deque([[begin]])
    while que:
        word = que.popleft()
        if target == word[-1]:
            return len(word) - 1
        for i in range(len(words)):
            if words[i] in word:
                continue
            result = check(word[-1], words[i])
            if result == 0:
                continue
            elif result == 1:
                temp = word.copy()
                temp.append(words[i])
                que.append(temp)          
    return 0

print(solution(	"hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))