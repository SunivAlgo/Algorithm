def solution(cacheSize, cities):
    answer = 0

    if cacheSize == 0:
        return 5 * len(cities)

    d = {}
    now = 0
    time = 1
    for i in cities:
        i = i.upper()
        if not i in d or d[i] == 0:
            if now < cacheSize:
                now += 1
            else:
                min = 100001
                city = ""
                for j in d:
                    if d[j] < min and d[j] != 0:
                        min = d[j]
                        city = j
                d[city] = 0
            d[i] = time
            time += 1
            answer += 5

        else:
            d[i] = time
            time += 1
            answer += 1
        print(d)
    return answer

cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(cacheSize, cities))


'''
대중적인 풀이를 보니 deque나 리스트를 활용하여 단순하게 리스트나 데큐에 값이 있으면 제거하고
뒤에 append 하는 삭으로 했다. 처음에 이 생각을 했지만 remove 과정에서 리스트를 사용할 경우 뒤에 있는 값들을 한칸씩 떙겨와야
하기 때문에 매우 느릴 것으로 생각하였고 deque는 애초에 remove가 있는지 몰라서 다른 방법으로 시도해서 많이 해맸다. (deque는 연결리스트로 구현되어 있다.)

그래서 나의 풀이는 그냥 딕셔너리를 하나 만들어서 값을 시간에 맞춰서(시간은 값을 넣을때 마다 1증가) 값을 넣고 넣기 전에 값이 있을 경우는
값을 바꿔주고 가장 늦게 넣은 값을 빼야할때는 딕셔너리의 값을 0으로 바꾸고 0일 시에는 캐시에 없다는 형식으로 했다. 그런데 최소 시간에 들어온
값을 찾는 경우에도 어차피 시간은 느리게 작동하는 것 같다.
'''

'''
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = deque()
    q_size = 0

    if cacheSize == 0:
        return 5 * len(cities)
    
    for i in cities:
        i = i.upper()
        hit = False
        for j in range(0, len(q)):
            if i == q[j]:
                hit = True
                if j == 0:
                    q.popleft()
                else:
                    q[j] = ""
                q.append(i)
                answer += 1
                break
        
        if not hit:
            if q_size >= cacheSize:
                q.popleft()
                while len(q) > 0 and q[0] == "":
                    q.popleft()
            else:
                q_size += 1
            q.append(i)
            answer += 5
        print(q)
    return answer
'''
