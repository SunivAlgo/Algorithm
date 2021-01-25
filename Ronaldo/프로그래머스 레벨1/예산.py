def solution(d, budget):
  
    answer = 0

    d.sort()
    for i in range(0,len(d)):
        if d[i] > budget:
            break
        budget -= d[i]
        answer += 1
    return answer