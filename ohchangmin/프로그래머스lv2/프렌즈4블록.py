def solution(m, n, board):
    answer = 0
    char_board = [list(board[i]) for i in range(len(board))]  # board의 값은 문자열로 이루어져 문자열 안의 문자의 변경이 힘들기 때문에 모두 문자로 바꿔서 이차원리스트에 저장

    while True:
        check = [[False] * n for _ in range(m)]   # board 크기 만큼 False로 채워진 이차원 리스트 생성
        flag = False
        for i in range(n-1):  #4칸의 같은 부분이 존재 하면 char_board의 인덱스 위치를 check 인덱스 위치에 대입하여 true로 바꿔준다(true는 제거되는 부분을 의미)
            for j in range(m-1):
                if char_board[i][j] != '0' and char_board[i][j] == char_board[i][j+1] and char_board[i][j] == char_board[i+1][j] and char_board[i][j] == char_board[i+1][j+1]:
                    check[i][j] = check[i+1][j] = check[i][j+1] = check[i+1][j+1] = True
                    flag = True 
        if not flag:    # 제거할 부분이 없을 경우 종료
            break

        for i in reversed(range(n)):    # 맨 아래의 인덱스 부터 채워져야 하기 때문에 역순으로 반복문 돌림
            for j in reversed(range(m)):
                if check[i][j]:     # 제거된 부분이라면 그 위에 있는 인덱스를 올라가며 순회하고 채워야할 문자를 찾는다.
                    for k in reversed(range(i)): 
                        if not check[k][j] and char_board[k][j] != '0':     #조건 = 제거된 부분이 아니며 0이 아닌곳(0은 비어있음을 의미한다.)
                            char_board[i][j] = char_board[k][j] # 위에 있는 올바른 값으로 채운 후 그 부분은 0으로 바꿔줌
                            char_board[k][j] = '0'  
                            break
                    else:
                        char_board[i][j] = '0'  # 만약 채울 값이 없다면 0으로 채움(제거된 부분위에 아무 값도 없다는 뜻)

        for i in check: # 제거된 부분만큼 answer를 더함
            for j in i:
                if j:
                    answer += 1

    return answer

m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m, n, board))

'''
check = [[False] * n] * m 이런식으로 선언할경우 check[0][0] 을 바꿀경우 이차원 배열 안의 모든 첫번째 원소가 바뀜
'''