from queue import PriorityQueue

def dijkstra(road, n, k):
    distance = [k+1 for i in range(n+1)]
    distance[1] = 0
    pq, road = PriorityQueue(), sorted(road)
    pq.put([0, 1])

    while not pq.empty():
        c,loc = pq.get()
        if c > distance[loc]: continue

        for x in road:
            if x[0] == loc or x[1] == loc:
                
                if x[0] == loc: dest, nextc = x[1], x[2]+c
                else: dest, nextc = x[0], x[2]+c

                if nextc < distance[dest]:
                    distance[dest] = nextc
                    pq.put([nextc,dest])

    return distance

def solution(N, road, K):
    answer = 0
    findD = dijkstra(road,N,K)
    for d in findD:
        if d<=K: answer+=1
    return answer

# https://blog.naver.com/leemyo_/222279372688