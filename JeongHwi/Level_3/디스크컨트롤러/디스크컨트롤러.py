# 첫 작업은 무조건 수행됨
import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
            	# [작업의 소요시간, 작업이 요청되는 시점]
                heapq.heappush(heap, [j[1], j[0]]) 
                # print(heap,start,now)

        if len(heap) > 0: # 처리할 작업이 있는 경우
            current = heapq.heappop(heap)
            start = now             # 그 전 작업이 끝난 시간 대입
            now += current[0]       # 총 작업의 소요시간
            answer += (now - current[1])    # 현재시간-작업이 요청되는 시점
            # print(heap,start,now,"if")
            i += 1
        else:
            now += 1
    return int(answer / len(jobs))

# 못품
print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]), 14)
# print(solution([[0, 10], [2, 12], [9, 19], [15, 17]]), 25)
# print(solution([[0, 3], [1, 9], [2, 6]]), 9)
# print(solution([[0, 1]]), 1)
# print(solution([[1000, 1000]]), 1000)
# print(solution([[0, 1], [0, 1], [0, 1]]), 2)
# print(solution([[0, 1], [0, 1], [0, 1], [0, 1]]), 2)
# print(solution([[0, 1], [1000, 1000]]), 500)
# print(solution([[100, 100], [1000, 1000]]), 500)
# print(solution([[10, 10], [30, 10], [50, 2], [51, 2]]), 6)
# print(solution([[0, 3], [1, 9], [2, 6], [30, 3]]), 7)