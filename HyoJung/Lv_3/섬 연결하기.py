def solution(n, costs):
    costs.sort(key = lambda x:x[2])
    bag, answer = set([costs[0][0]]), 0
    
    while len(bag)!=n:
        for i in costs:
            if i[0] in bag and i[1] in bag:
                continue
            if i[0] in bag or i[1] in bag:
                bag.update([i[0],i[1]])
                answer+=i[2]
                break
    
    return answer

# https://blog.naver.com/leemyo_/222297102578