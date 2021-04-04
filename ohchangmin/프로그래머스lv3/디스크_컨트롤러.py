import heapq

def solution(jobs):
    answer, now, i = 0,0,0
    start = -1
    heap = []

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            i += 1
        else:
            now += 1
    
    return int(answer / len(jobs))

    
#print(solution([[0, 3], [1, 9], [2, 6]])) 
#print(solution([[0, 1], [1, 2], [500, 6]])) 
print(solution([[0, 4], [0, 3], [0, 2], [0, 1]])) 
print(solution([[0, 1], [0, 2], [0, 3], [0, 4]])) 
#print(solution([[0, 5], [1, 2], [5, 5]])) 

'''
못품
순서의 기준을 찾지 못했다.
'''