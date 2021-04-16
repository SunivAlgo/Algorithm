def solution(n, results):
    wins, loses = {}, {}
    
    for i in range(1, n+1):
        wins[i], loses[i] = set(), set()      
    
    
    for i in range(1, n+1):                    
        for r in results:                      
            if r[0] == i:                      
                wins[i].add(r[1])
            if r[1] == i:
                loses[i].add(r[0])
        for winner in loses[i]:             
            wins[winner].update(wins[i])
        for loser in wins[i]:
            loses[loser].update(loses[i]) 
        print("wins", wins)
        print("loses", loses)
        print()


    cnt = 0
    for i in range(1, n+1):                   
        if len(wins[i]) + len(loses[i]) == n-1:
            cnt += 1
            
    return cnt

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))