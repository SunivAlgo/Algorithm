def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0
    cache = dict()
    for i in cities:
        city = i.lower()
        if city not in cache:
            if len(cache) == cacheSize:
                del cache[list(cache.keys())[0]]
            cache[city] = 0
            answer += 5
        else:
            del cache[city]
            cache[city] = 0
            answer += 1

    return answer

print(solution(	2, ["Jeju", "Pangyo", "NewYork", "newyork"]))