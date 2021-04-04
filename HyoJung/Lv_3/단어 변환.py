def solution(begin, target, words):
    if target not in words: return 0
    
    s, answer = [begin], 0
    while s:
        now = s.pop()
        if now == target: return answer
    
        for i,x in enumerate(words):
            
            dif_alpha=0
            if words[i]=="-": continue
                
            for j in range(len(x)):
                if x[j]!=now[j]: dif_alpha+=1
            if dif_alpha == 1:
                s.append(x)
                words[i] = "-"
        answer+=1

# https://blog.naver.com/leemyo_/222298412053