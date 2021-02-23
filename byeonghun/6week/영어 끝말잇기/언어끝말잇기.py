def solution(n, words):
    player = {}
    word = {}
    prev = ''
    for i in range(n):
        player[i+1] = 0
    for i , v in enumerate(words):
        if prev and prev[-1] != v[0]:
            return [i % n + 1, player[i % n + 1] + 1]
        prev = v
        if v in word:
            return [i % n + 1, player[i % n + 1] + 1]
        else:
            word[v] = 0
            player[i % n + 1] += 1

    return [0,0]