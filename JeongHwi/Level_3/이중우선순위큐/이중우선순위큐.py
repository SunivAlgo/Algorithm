"""
명령어
I 숫자 - INSERT
D 1 - 최대값 삭제
D -1 - 최솟값 삭제
"""
import heapq as hq

def solution(operations):
    heap = []
    for o in operations:
        op,num = o.split()
        if op == "I":
            hq.heappush(heap,int(num))
        else:
            if not heap:
                continue
            if num == "1":
                hq._heapify_max(heap) # O(nlogn)
                hq._heappop_max(heap) 

            elif num == "-1":
                hq.heapify(heap)
                hq.heappop(heap)
    if heap:
        hq.heapify(heap)
        min_ = hq.heappop(heap)
        if not heap:
            max_ = min_
        else:
            hq._heapify_max(heap)
            max_ = hq.heappop(heap)
        return [max_,min_]
    else:
        return [0,0]
print(solution(["I 16","D 1"]),[0,0])
print(solution(["I 7","I 5","I -5","D -1"]),[7,5])
