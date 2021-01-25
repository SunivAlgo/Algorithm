 def check_list(li):
        count = 0
        if len(li) >= 2:
            if(li[-1] == li[-2]):
                del(li[-1])
                del(li[-1])
                count += 2
        return count
def solution(board, moves):
    doll_list = []
    answer = 0

   


    for i in range(0,len(moves)):
        moves[i] -= 1

    for i in moves:
        for j in range(0 , len(board)):
            if board[j][i] != 0:
                doll_list.append(board[j][i])
                board[j][i] = 0
                answer += check_list(doll_list)
                break
    return answer