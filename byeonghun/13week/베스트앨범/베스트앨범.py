def solution(genres, plays):
    d = {}
    answer = []
    for i in range(len(plays)):
        if genres[i] not in d:
            d[genres[i]] = [plays[i],[i]]
        else:
            d[genres[i]][1].append(i)
            d[genres[i]][0] += plays[i]
    for i in d.keys():
        d[i][1].sort(key= lambda x : (plays[x],-x))
    l = list(d.keys())
    l.sort(key= lambda x: d[x][0], reverse=True)
    for key in l:
        for i in range(2):
            if d[key][1]:
                answer.append(d[key][1].pop())
            else: break
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))