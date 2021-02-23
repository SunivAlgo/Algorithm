def solution(n, words):
    answer = [0, 0]
    d = {}

    before = ""
    for i in range(0, len(words)):
        if i != 0 and words[i][0] != before or words[i] in d:
            answer[0] += i%n+1
            answer[1] += i//n+1
            break
        if not words[i] in d:
            d[words[i]] = 1
        before = words[i][-1]
    return answer

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

print(solution(n, words))

'''
딕셔너리로 중복확인
for문의 i를 n으로 나누거나 나머지를 활용하여 번호와 차례 부여함
before 변수로 그 전 단어 데이터 저장
'''