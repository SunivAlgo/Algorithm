from copy import copy
def solution(dirs):
    answer = 0
    point_now = [0,0] ## 현재 point
    direction_dict = {'U':[1,0] , 'L':[0,-1], 'R':[0,1], 'D':[-1,0]}
    save_path = [] ## 경로저장 리스트

    for dir in dirs:
        value = direction_dict[dir]
        x_for_calculation = point_now[0] + value[0] ## 계산하였을 때의 임시 x좌표
        y_for_calculation =  point_now[1] + value[1] ## 계산하였을 때의 임시 y좌표

        if x_for_calculation < -5 or x_for_calculation > 5 or \ 
            y_for_calculation < -5 or y_for_calculation > 5: ## x,y가 -5~5 를 벗어나면 skip
            continue
        
        temp_list = [x_for_calculation,y_for_calculation] ## 이동할 좌표를 담은 임시 list

        ## 경로 저장을 [0,0]->[0,1] 이라 하면 ([0,0],[0,1]) tuple을 만든 후 save_path에 삽입
        if not save_path : ##이동경로가 없다면 -> dirs의 첫 원소 검사시
            save_path.append((point_now, temp_list)) ## 경로저장
            point_now = copy(temp_list) ## 현재 point 이동
            answer += 1 ## answer + 1
            continue

        for tu in save_path: ## 저장된 경로 순회
            if point_now in tu and temp_list in tu: ## 시작점과 끝점이 튜플 내에 있다면 break
                break
        else: ## 없으면 경로저장, answer += 1
            save_path.append((point_now, [x_for_calculation,y_for_calculation]))
            answer += 1
        
        point_now = copy(temp_list)
    return answer

print(solution("ULURRDLLU"))