def solution(n, computers):
    answer = 0
    network_list = [set([k]) for k in range(n)]
    
    for x in range(len(computers)):
        for y in range(len(computers[0])):
            if x >= y: continue

            if computers[x][y] == 1:
                x_index = -1
                y_index = -1
                for network_index in range(len(network_list)):
                    if x in network_list[network_index]:
                        x_index = network_index
                    if y in network_list[network_index]:
                        y_index = network_index
                    if x_index != -1 and y_index != -1:
                        break
                if x_index == y_index:
                    continue
                network_list[x_index] = network_list[x_index].union(network_list[y_index])
                del(network_list[y_index])
                

    answer = len(network_list)
    return answer

print(solution(5, [[1, 1, 0, 0, 0], [1, 1, 0,0,0], [0, 0, 1,0,0,],[0, 0, 1,1,0,],[0, 0, 1,0,1,]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))