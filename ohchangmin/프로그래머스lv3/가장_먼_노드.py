from collections import deque

def solution(n, edge):
    d = {}      # 딕셔너리에 모든 노드에 연결된 다른 노드들을 배열로 정리 하여 저장 (이렇게 미리 만들지 않으면 나중에 시간초과 발생)
                # ex) {1: [3, 2], 2: [3, 1, 4, 5], 3: [6, 4, 2, 1], 4: [3, 2], 5: [2], 6: [3]}
    for i in range(1, n+1):
        d[i] = []
    for e in edge:
        d[e[0]].append(e[1])
        d[e[1]].append(e[0])

    check = [False] * (n+1)     # 방문 했는지 유무 검사용
    q = deque()         
    check[1] = True     # 1을 큐에 넣으며 시작
    q.append(1)
    size = 1

    while q:    #큐가 빌때까지
        size = len(q)      
        for _ in range(size):   #반복문 시작시 큐의 사이즈 만큼 pop을 함 (시작 시 큐에 있는 원소들은 거리가 같음)
            p = q.popleft()
            for i in d[p]:      #딕셔너리에 저장된 데이터들을 가지고 방문했는지 유무에 따라 q에 원소를 넣음
                if not check[i]:
                    q.append(i)
                    check[i] = True
         
    return size

n = 6	
vertex	= [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n, vertex))