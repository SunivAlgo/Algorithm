from collections import deque

def solution(N, road, K):
    answer = 0
    dist = [-1 for i in range(N+1)]     # 거리를 저장하는 리스트, -1은 방문하지 않음을 의미
    
    q = deque([1])      # 첫 시작점을 큐에 넣고 거리는 0으로 설정
    dist[1] = 0

    while q:
        p = q.popleft()     #큐를 팝하면서 연산 진행

        for i in road:      #road의 첫번째, 두번째 인덱스에 팝한 숫자가 있다면 서로 다른 시작점 끝점 변수를 두어 연산진행
            if i[0] == p:
                start = i[0]
                end = i[1]
                d = i[2]
                if dist[end] == -1 or dist[end] > dist[start] + d:      #방문하지 않았거나 시작점 + 거리가 끝점에 저장된 거리보다 작을시에 거리를 업데이트 해준 후 q에 추가
                    dist[end] = dist[start] + d
                    q.append(end)
            if i[1] == p:
                start = i[1]
                end = i[0]
                d = i[2]
                if dist[end] == -1 or dist[end] > dist[start] + d:
                    dist[end] = dist[start] + d
                    q.append(end)

    for i in range(1, N+1): 
        if dist[i] <= K:
            answer += 1
    return answer

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
print(solution(N, road, K))

N = 6
road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
K = 4
print(solution(N, road, K))