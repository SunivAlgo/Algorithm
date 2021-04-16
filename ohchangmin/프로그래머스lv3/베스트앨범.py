def solution(genres, plays):
    answer = []
    s = {}      # {'classic': 1450, 'pop': 3100} 이런식으로 저장
    d = {}      # {'classic': [[0, 500], [2, 150], [3, 800]], 'pop': [[1, 600], [4, 2500]]} 이런식으로 저장
    
    for i in range(len(plays)):
        if not genres[i] in s:
            s[genres[i]] = plays[i]
        else:
            s[genres[i]] += plays[i]
        if not genres[i] in d:
            d[genres[i]] = [[i, plays[i]]]
        else:
            d[genres[i]].append([i, plays[i]])

    sumArr = []
    for i in s:     #s를 정렬하기 위해 리스트로 변환
        sumArr.append([i, s[i]])    
    sumArr = sorted(sumArr, key= lambda x: x[1], reverse=True)
    
    for i in d:     #d의 요소들 다 내림차순 정렬
        d[i] = sorted(d[i], key= lambda x: x[1], reverse=True)

    for i in sumArr:    #두개씩 추가
        cnt = 0
        for j in d[i[0]]:
            answer.append(j[0])
            cnt += 1
            if cnt == 2:
                break

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))