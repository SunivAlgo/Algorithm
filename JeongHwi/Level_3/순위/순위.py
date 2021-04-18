def solution(n,results):
    # init array

    score = [[float("inf") for _ in range(n)] for _ in range(n)]

    for i in range(n):
        score[i][i] = 0
    for win,lose in results:
        score[lose-1][win-1] = 1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if score[i][j] > score[i][k] + score[k][j]:
                    score[i][j] = score[i][k] + score[k][j]
    
    count = 0
    for i in range(n):
        flag = False
        for j in range(n):
            if score[i][j] != float("inf") or score[j][i] != float("inf"):
                flag = True
            else:
                flag = False
                break
        if flag:
            count += 1
    return count

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))

# 질문하기를 보고 푼 문제
"""
# 왜 플로이드 와샬을 사용하는가?
우선은 등수를 체크 가능할 때에는 경기를 모두 마친 사람만 가능
플로이드 와샬의 경우 노드를 거쳐가는 모든 경우의수를 체크한다.
"""