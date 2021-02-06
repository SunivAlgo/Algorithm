import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        minheap = heapq.heappop(scoville)
        heapq.heappush(scoville, minheap + (heapq.heappop(scoville) * 2))
        answer += 1
    return answer
print(solution([1, 2, 3, 9, 10, 12]	, 7))