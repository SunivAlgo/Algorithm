def solution(n, computers):
    answer = 0
    network_list = [set([k]) for k in range(n)] ## 네트워크 망을 넣어두는 리스트, 일단 초기값은 ex) 1,2,3,4 일시 [{1},{2},{3},{4}]
    
    for x in range(len(computers)):
        for y in range(len(computers[0])):
            if x >= y: continue ## 어차피 행렬이 대각선을 기준으로 대칭이니까 각 행마다 x == y인 후의 열부터 검사

            if computers[x][y] == 1: ## 1이면 x 노드와 y 노드가 연결되어있다는 뜻
                x_index, y_index = -1, -1 ## 초기값 설정 (network_list 내에서 x, y 가 들어있는 집합이 어느 index인지 저장하기 위해 설정)
                for network_index in range(len(network_list)):
                    if x in network_list[network_index]: ## x 원소가 해당 집합 내에 있을 시, x_index 저장
                        x_index = network_index
                    if y in network_list[network_index]: ## y 원소가 해당 집합 내에 있을 시, y_index 저장
                        y_index = network_index
                    if x_index != -1 and y_index != -1: ## x,y 가 들어있는 집합을 찾았을 경우 break
                        break
                if x_index == y_index: ## x_index == y_index 면 애초에 x,y가 들어있는 집합이 같았을 경우.
                    continue
                network_list[x_index] = network_list[x_index].union(network_list[y_index]) ## x_index != y_index 이면 합집합해버리기
                del(network_list[y_index])
                

    answer = len(network_list) ##network_list 내에 있는 네트워크 망의 개수가 정답이다.
    return answer

print(solution(5, [[1, 1, 0, 0, 0], [1, 1, 0,0,0], [0, 0, 1,0,0,],[0, 0, 1,1,0,],[0, 0, 1,0,1,]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))