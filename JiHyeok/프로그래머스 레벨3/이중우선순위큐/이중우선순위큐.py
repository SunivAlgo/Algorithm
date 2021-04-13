import heapq
def solution(operations):
    answer = []
    for i in range(len(operations)):
        operations[i] = operations[i].split(' ')
        operations[i][1] = int(operations[i][1])

    heap = []

    for operation in operations:
        if operation[0] == 'I':
            heapq.heappush(heap,operation[1])
        elif operation[0] == 'D':
            if not heap:
                continue
            if operation[1] == -1:
                heapq.heappop(heap)
            elif operation[1] == 1:
                heap.remove(max(heap))
                heapq.heapify(heap)
    if not heap:
        answer = [0,0]
        return answer
    answer = [max(heap),heap[0]]
    return answer


print(solution(["I 16","D 1"]))
print(solution(["I 7","I 5","I -5","D -1"]))