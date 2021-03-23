check = []

def dfs(now, computers):    # dfs를 통해 깊게 모든것을 탐색하면서 연결되어 있는 곳은 check에 방문을 적는다
    global check
    check[now] = True   # 방문 확인

    for i in range(len(computers[now])):
        if computers[now][i] == 1 and not check[i]:     #연결되어 있으며 아직 방문하지 않았다면 dfs 들어감
            dfs(i, computers)


def solution(n, computers):
    answer = 0
    global check
    check = [False] * n

    for start in range(len(computers)):
        if not check[start]:    #아직 연결 되어 있지 않는 곳이 있으면 answer+1 을 하고 dfs에 들어간다.
            answer += 1
            dfs(start, computers)

    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))