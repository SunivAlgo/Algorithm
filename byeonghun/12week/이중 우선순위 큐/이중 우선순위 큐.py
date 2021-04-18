import heapq
import math
def max_return(heap):
    n = math.ceil((len(heap) ** 0.5))
    if n < 3:
        maxi = 0
        for i in range(len(heap)):
            if heap[i] > heap[maxi]:
                maxi = i
        heap[maxi] , heap[-1] = heap[-1] , heap[maxi]
        return heap

    if len(heap) - (2 ** (n - 1)) > (2 ** (n - 1)) // 2:
        maxi = 2 ** (n - 1) - 1
        for i in range(2 ** (n - 1) - 1, len(heap)):
            if heap[i] > heap[maxi]:
                maxi = i
        heap[maxi] , heap[-1] = heap[-1] , heap[maxi]
    else:
        maxi = 2 ** (n - 1) - 2 ** (n - 3) - 1
        for i in range(2 ** (n - 1) - 2 ** (n - 3) - 1, len(heap)):
            if heap[i] > heap[maxi]:
                maxi = i
        heap[maxi] , heap[-1] = heap[-1] , heap[maxi]
    return heap
def solution(operations):
    answer = []
    heap = []
    for operation in operations:
        temp = operation.split(" ")
        if temp[0] == "I":
            heapq.heappush(heap, int(temp[1]))
        else:
            if int(temp[1]) == 1:
                if heap:
                    heap = max_return(heap)
                    heap.pop()
            else:
                if heap:
                    heapq.heappop(heap)
    print(heap)
    if len(heap) == 1:
        return [heap[0], heap[0]]
    elif len(heap) == 0:
        return [0,0]
    else:
        heap = max_return(heap)
        return [heap[-1], heapq.heappop(heap)]

print(solution(["I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1", "I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1"]))