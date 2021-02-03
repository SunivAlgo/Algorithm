def solution(n):
    temp = n
    answer = []
    li=[]
    a=0
    b=0
    number = 1

    for c in range(0,n):
        l = [0] * (c+1)
        li.append(l)
    
    

    for i in range(0,n):
        if i % 3 == 0:
            for j in range(0,temp):
                li[a][b] = number
                number += 1
                if j == temp -1:
                    break
                
                a += 1
                
            b += 1        

        elif i % 3 == 1:
            for j in range(0,temp):
                li[a][b] = number
                number += 1
                if j == temp -1:
                    break
                
                b += 1
            a -= 1
            b -= 1

        elif i % 3 == 2:
            for j in range(0,temp):
                li[a][b] = number
                number += 1
                if j == temp -1:
                    break
                
                a -= 1
                b -= 1
            a += 1
        
            
        temp = temp -1


    li = sum(li,[])

    return li

print(solution(5))