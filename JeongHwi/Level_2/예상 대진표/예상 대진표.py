def solution(N,A,B):
    league = [x for x in range(1,N+1)]
    count = 0
    while True:
        new_League = []
        team = 1
        for i in range(0,len(league),2):
            new_League.append(team)
            if league[i] == A:
                if league[i+1] == B:
                    return count+1
                A = team
            elif league[i] == B: 
                if league[i+1] == A:
                    return count+1
                B = team
            elif league[i+1] == A:
                if league[i+1] == B:
                    return count+1
                A = team
            elif league[i+1] == B:
                if league[i+1] == A:
                    return count+1
                B = team
            team+=1
        count+=1
        league = new_League

print(solution(8,4,7))