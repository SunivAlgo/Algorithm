def solution(cacheSize, cities):
    answer = 0
    if cacheSize==0: return len(cities)*5
    cache=[""]*cacheSize

    for city in cities:
        c=city.lower()
        if c not in cache:
            del cache[0]
            answer+=5
        else:
            idx=cache.index(c)
            del cache[idx]
            answer+=1
        cache.append(c)

    return answer

# https://blog.naver.com/leemyo_/222264448043