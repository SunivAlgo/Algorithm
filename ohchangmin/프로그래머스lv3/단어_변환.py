answer = 50

def dfs(now, target, words, check, cnt):
    if now == target:
        global answer
        if answer > cnt:    #최소한의 방법 
            answer = cnt
        return

    for i in range(len(words)):
        count = 0
        if not check[i]:    # 한글자 다른 지 비교
            for j in range(len(now)):
                if now[j] != words[i][j]:
                    count += 1

        if count == 1:
            check[i] = True
            dfs(words[i], target, words, check, cnt+1)
            check[i] = False    # 해줘야 다른 경우의 수도 찾기 가능


def solution(begin, target, words):

    if not target in words:
        return 0

    check = [False] * len(words)
    dfs(begin, target, words, check, 0)
    
    return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))