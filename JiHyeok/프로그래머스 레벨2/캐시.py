from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache_deque = deque() ##    cache 설정
    ##  cacheSize = 0 이면 모두 cachemiss
    if cacheSize == 0:
        return 5 * len(cities)
    

    for s in cities:
        city = s.upper() ## city는 이제 전부 대문자인 도시명
        
        ##  city가 cache에 있을때
        if city in cache_deque:
            cache_deque.remove(city)
            cache_deque.append(city)
            answer += 1

        ##  city가 cache에 없을때
        else:
            ##  cache가 꽉 찬 경우
            if len(cache_deque) >= cacheSize:
                cache_deque.popleft()
                cache_deque.append(city)
            ##  cache에 자리가 있는 경우
            else:
                cache_deque.append(city)
            answer += 5


    return answer

print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
