import heapq

def solution(operations):
    minq = []
    maxq = []
    size = 0
    i = 0   # 최소힙과 최대힙에 데이터가 나눠져 있기 때문에 나눠진 데이터의 같은 요소들을 구분하기 위해 넣음
    d = {}  # 최소힙 최대힙 각각에 데이터가 유령 데이터인지 파악 
    for operation in operations:
        split_operation = operation.split()
        num = int(split_operation[1])
        if split_operation[0] == 'I':
            heapq.heappush(minq, (num, i))      # 최소힙 최대힙에 데이터를 넣음 i를 넣음으로써 같은 데이터인지 파악 
            heapq.heappush(maxq, (-num, num, i))
            d[i] = 1    # 딕셔너리에 i를 넣어 i를 가진 데이터는 큐에 양 큐에 존재한다
            size += 1   # 큐 사이즈 파악
            i += 1      # i 바꿈
        elif size > 0:   
            if num == 1:
                while d[maxq[0][2]] == 0:   #pop 할때 유령 데이터라면 다 걸러줌
                    heapq.heappop(maxq)
                d[maxq[0][2]] = 0   # 큐에 존재하는 값이 아니라고 선언
                heapq.heappop(maxq) # 큐에 있는 진짜 값을 지움
            else:
                while d[minq[0][1]] == 0:
                    heapq.heappop(minq)
                d[minq[0][1]] = 0
                heapq.heappop(minq)
            size -= 1   # 팝을 했기 때문에 사이즈 1 줄임

    if size == 0:
        return [0,0]
        
    while d[maxq[0][2]] == 0:   #나머지 유령데이터를 팝해줌
        heapq.heappop(maxq)
    while d[minq[0][1]] == 0:
        heapq.heappop(minq)
    else:
        return [maxq[0][1] ,minq[0][0]]