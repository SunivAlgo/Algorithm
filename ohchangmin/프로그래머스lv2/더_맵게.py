import heapq

def solution(scoville, K):
    answer = 0
    heap = scoville
    heapq.heapify(heap)

    while heap[0] < K:
        if len(heap) == 1:
            return -1
        f = heapq.heappop(heap)
        s = heapq.heappop(heap)
        mix = f + s*2
        heapq.heappush(heap, mix)
        answer += 1

    return answer 

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))

'''
파이썬은 힙을 쉽게 만들 수 있어서 어려움이 없었다.
값들을 전부 힙으로 구성한후 계산을 진행하고 힙의 크기가 1일경우는
더 큰 수 를 만들수가 없어서 -1를 리턴한다.
'''