from collections import deque
def solution(cacheSize,cities):
    cache = deque()
    time = 0
    if cacheSize == 0:
        return len(cities)*5
    for city in cities:
        city = city.lower()
        cacheLen = len(cache)
        if cacheLen >= cacheSize:
            if city in cache:
                time+=1
                cache.remove(city)
                cache.append(city)
            else:
                if cache:
                    cache.popleft()
                cache.append(city)
                time+=5
        elif cacheLen < cacheSize:
            if city not in cache:
                cache.append(city)
                time+=5
            else:
                if cache:
                    cache.remove(city)
                cache.append(city)
                time+=1
    return time
        


print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(5,["seoul","SEOUL","SEOUL"]))
print(solution(2,["a","a","b","b","c"]))
print(solution(0,["a","a","a","a"]))
print(solution(3,["a","b","a"]))