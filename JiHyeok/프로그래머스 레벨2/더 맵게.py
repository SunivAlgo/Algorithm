import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    heapq.heapify(scoville)
    while heap[0] < K and len(heap) > 1:
        m1 = heapq.heappop(heap)
        m2 = heapq.heappop(heap)
        s = m1 + m2 * 2
        heapq.heappush(heap,s)
        answer += 1
    if heap[0] < K:
        return -1


    return answer

print(solution([1, 2, 3, 9, 10, 12],7))


'''
    1.  heap정렬을 써야 하는 문제입니다.
    2.  일단 heap리스트에 scoville의 원소를 heappush를 모두 해줍니다.
    3.  heap리스트의 길이가 2 이상이고 최솟값(heap[0])이 K보다 작은 동안,
        m1 = heappop
        m2 = heappop
        s = m1 + m2 *2 
        heappush(heap,s)를 구현
    4.  모든 원소를 돌렸음에도 heap[0]이 K보다 작으면 불가능한 경우이므로 -1 return
'''