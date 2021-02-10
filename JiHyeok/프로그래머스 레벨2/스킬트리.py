from collections import deque
def solution(skill, skill_trees):
    answer = 0
    switch = 0
    Q = deque()

    for i in skill_trees:
        for j in range(0,len(skill)):
            index = i.find(skill[j])
            if index == -1:
                index = 27
            Q.append(index)
        
        while len(Q) >= 2:
            if Q[0] > Q[1]:
                switch = 1
                break
            Q.popleft()
        
       

        if switch == 0:
            answer += 1
            
        Q = deque()
        switch = 0
    

    


    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))


'''
    
'''