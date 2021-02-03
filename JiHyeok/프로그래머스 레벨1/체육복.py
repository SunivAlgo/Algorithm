def solution(n, lost, reserve):
    
    lost.sort()
    reserve.sort()
    answer = 0
    list_n = []

    for i in range(1,n+1):
        list_n.append(i)

    for i in range (0, len(reserve)):
            for j in range (0, len(lost)):
                if reserve[i] == lost[j]:
                    lost[j] = -1
                    reserve[i] = -1
                    break


    for i in range (0, len(reserve)):
        for j in range (0, len(lost)):
            if (lost[j] - 1 <= reserve[i] <= lost[j] + 1) or lost[j] == -1:
                del(lost[j])
                break




    if lost:
        for i in lost:
            list_n.remove(i)

    answer = len(list_n)
        


    return answer