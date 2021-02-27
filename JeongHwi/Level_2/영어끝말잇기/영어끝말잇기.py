# 탈락조건
"""
1. 중복된 단어를 말할 때
2. 앞사람이 말한 단어의 마지막문자가 아닐 때
"""
def solution(n,words):
    word = dict()
    turn = 0
    lastSpell = ""
    for i,w in enumerate(words):
        if i%n == 0:
            turn += 1
        now = (i%n)+1
        if w not in word:
            word[w] = 1
        else:
            return [now,turn]
        #초기 설정
        if lastSpell == "":
            lastSpell += w[-1]
            continue
        if lastSpell != w[0]:
            return [now,turn]
        else:
            lastSpell = w[-1]
    return [0,0]
        

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))